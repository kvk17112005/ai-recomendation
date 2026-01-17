from flask import Flask, render_template, request, redirect, url_for, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sqlite3
import os
from datetime import datetime
import json

app = Flask(__name__, template_folder='templetes')
DB_FILE = 'recommendations.db'

# Initialize database
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # Topics table
    c.execute('''CREATE TABLE IF NOT EXISTS topics
                 (id INTEGER PRIMARY KEY, title TEXT UNIQUE, category TEXT, created_date TEXT)''')
    
    # Search history table
    c.execute('''CREATE TABLE IF NOT EXISTS search_history
                 (id INTEGER PRIMARY KEY, query TEXT, results TEXT, search_date TEXT)''')
    
    # Check if topics exist
    c.execute('SELECT COUNT(*) FROM topics')
    if c.fetchone()[0] == 0:
        default_topics = [
            ("Latest technology trends", "Technology"),
            ("AI in film editing", "AI & Media"),
            ("Personalized learning using AI", "Education"),
            ("Market trend analysis using data science", "Data Science"),
            ("Yoga and mental health", "Health & Wellness"),
            ("Blockchain and cryptocurrency", "Technology"),
            ("Machine learning in healthcare", "AI & Healthcare"),
            ("Web development with Python", "Programming"),
            ("Cloud computing architecture", "Infrastructure"),
            ("Natural language processing", "AI & NLP")
        ]
        for title, category in default_topics:
            c.execute('INSERT OR IGNORE INTO topics (title, category, created_date) VALUES (?, ?, ?)',
                     (title, category, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    
    conn.commit()
    conn.close()

init_db()

def get_topics():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT title FROM topics')
    topics = [row[0] for row in c.fetchall()]
    conn.close()
    return topics

def get_all_topics_with_category():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT id, title, category FROM topics')
    topics = c.fetchall()
    conn.close()
    return topics

contents = get_topics()
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(contents)

def save_search(query, results):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('INSERT INTO search_history (query, results, search_date) VALUES (?, ?, ?)',
             (query, json.dumps(results), datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []

    if request.method == "POST":
        user_input = request.form.get("query", "").strip()
        if user_input:
            user_vec = vectorizer.transform([user_input])
            similarity = cosine_similarity(user_vec, tfidf_matrix)
            
            # Get top 5 with scores
            top_indices = similarity[0].argsort()[-5:][::-1]
            recommendations = []
            for idx in top_indices:
                score = float(similarity[0][idx]) * 100
                recommendations.append({
                    'title': contents[idx],
                    'score': f"{score:.1f}%",
                    'category': get_topic_category(contents[idx])
                })
            
            save_search(user_input, [r['title'] for r in recommendations])

    return render_template("index.html", recommendations=recommendations)

def get_topic_category(title):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT category FROM topics WHERE title = ?', (title,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else "General"

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        action = request.form.get("action")
        
        if action == "add":
            title = request.form.get("title", "").strip()
            category = request.form.get("category", "").strip()
            if title and category:
                try:
                    conn = sqlite3.connect(DB_FILE)
                    c = conn.cursor()
                    c.execute('INSERT INTO topics (title, category, created_date) VALUES (?, ?, ?)',
                             (title, category, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                    conn.commit()
                    conn.close()
                    # Rebuild vectorizer
                    global contents, tfidf_matrix, vectorizer
                    contents = get_topics()
                    tfidf_matrix = vectorizer.fit_transform(contents)
                except Exception as e:
                    print(f"Error: {e}")
        
        elif action == "delete":
            topic_id = request.form.get("id")
            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            c.execute('DELETE FROM topics WHERE id = ?', (topic_id,))
            conn.commit()
            conn.close()
            # Rebuild vectorizer
            contents = get_topics()
            tfidf_matrix = vectorizer.fit_transform(contents)
    
    topics = get_all_topics_with_category()
    return render_template("admin.html", topics=topics)

@app.route("/history")
def history():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT query, results, search_date FROM search_history ORDER BY search_date DESC LIMIT 50')
    searches = c.fetchall()
    conn.close()
    
    history_data = []
    for query, results, date in searches:
        history_data.append({
            'query': query,
            'results': json.loads(results),
            'date': date
        })
    
    return render_template("history.html", history=history_data)

@app.route("/analytics")
def analytics():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # Total searches
    c.execute('SELECT COUNT(*) FROM search_history')
    total_searches = c.fetchone()[0]
    
    # Most searched queries
    c.execute('SELECT query, COUNT(*) as count FROM search_history GROUP BY query ORDER BY count DESC LIMIT 10')
    popular_queries = c.fetchall()
    
    # Total topics
    c.execute('SELECT COUNT(*) FROM topics')
    total_topics = c.fetchone()[0]
    
    # Topics by category
    c.execute('SELECT category, COUNT(*) FROM topics GROUP BY category')
    categories = c.fetchall()
    
    conn.close()
    
    return render_template("analytics.html", 
                         total_searches=total_searches,
                         popular_queries=popular_queries,
                         total_topics=total_topics,
                         categories=categories)

if __name__ == "__main__":
    app.run(debug=True)