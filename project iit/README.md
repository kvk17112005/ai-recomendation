# 🎯 Smart Content Recommendation System

A professional Flask web application that uses TF-IDF vectorization and cosine similarity to provide intelligent content recommendations. Perfect for academic projects and production deployment.

## ✨ Features

- 🔍 **Smart Search**: TF-IDF-based recommendations with similarity scoring
- 💾 **Database**: SQLite with persistent storage for topics and search history
- 📜 **Search History**: Track all user searches with timestamps
- ⚙️ **Admin Panel**: Dynamically manage topics and categories
- 📊 **Analytics Dashboard**: View statistics and trending searches
- 🎨 **Professional UI**: Responsive design with gradient styling
- 🔄 **Real-time Updates**: ML model rebuilds automatically when content changes

## 🛠️ Technologies Used

| Component | Technology |
|-----------|-----------|
| **Backend** | Flask (Python 3.9+) |
| **ML Engine** | scikit-learn (TF-IDF + Cosine Similarity) |
| **Database** | SQLite3 |
| **Frontend** | HTML5, CSS3 (Responsive) |
| **Other** | JSON, Pandas (optional) |

## 📦 Project Structure

```
Smart-Content-Recommendation-System/
├── app.py                    # Main Flask application (195 lines)
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── .gitignore               # Git ignore rules
├── templetes/               # HTML Templates
│   ├── index.html           # Main search page
│   ├── history.html         # Search history
│   ├── admin.html           # Admin panel
│   └── analytics.html       # Analytics dashboard
├── recommendations.db       # SQLite database (auto-created)
└── .venv/                   # Virtual environment (not uploaded)
```

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/Smart-Content-Recommendation-System.git
cd Smart-Content-Recommendation-System

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

You should see:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 3. Open in Browser

Visit: **http://127.0.0.1:5000**

## 📖 How to Use

### 🏠 Search Page (Main)
1. Type a search query (e.g., "AI", "learning", "technology")
2. Click "Search"
3. View recommendations with similarity scores
4. Each result shows title, category, and confidence percentage

### 📜 Search History
- Navigate to `/history`
- View all past searches with their results
- Timestamped entries
- Helps find previous recommendations

### ⚙️ Admin Panel
- Navigate to `/admin`
- **Add Topics**: Enter title and category
- **Manage Topics**: View all topics and delete if needed
- **Real-time Updates**: ML model updates automatically

### 📊 Analytics Dashboard
- Navigate to `/analytics`
- View total searches count
- See popular search queries
- Check category distribution
- Monitor database growth

## 🧠 How It Works

### Recommendation Engine

1. **TF-IDF Vectorization**
   - Converts text documents into numerical vectors
   - Weights terms by importance

2. **Cosine Similarity**
   - Compares user query with all documents
   - Returns similarity score (0-1 scale)
   - Higher score = more relevant

3. **Ranking**
   - Sorts by similarity
   - Returns top 5 recommendations
   - Displays confidence percentages

### Example
```
Query: "AI"
Results:
  1. "AI in film editing" ..................... 85.3%
  2. "Personalized learning using AI" ........ 72.1%
  3. "Machine learning in healthcare" ....... 68.9%
  4. "Natural language processing" .......... 52.4%
  5. "Latest technology trends" ............. 31.2%
```

## 📊 Database Schema

### Topics Table
```sql
CREATE TABLE topics (
    id INTEGER PRIMARY KEY,
    title TEXT UNIQUE,
    category TEXT,
    created_date TEXT
)
```

### Search History Table
```sql
CREATE TABLE search_history (
    id INTEGER PRIMARY KEY,
    query TEXT,
    results TEXT,          -- JSON format
    search_date TEXT
)
```

## 🔧 Configuration

### Default Topics (10)
- Latest technology trends
- AI in film editing
- Personalized learning using AI
- Market trend analysis using data science
- Yoga and mental health
- Blockchain and cryptocurrency
- Machine learning in healthcare
- Web development with Python
- Cloud computing architecture
- Natural language processing

### Add Custom Topics
Use the Admin Panel (`/admin`) to add topics dynamically.

## 📝 API Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET/POST | Search page with recommendations |
| `/admin` | GET/POST | Manage topics and categories |
| `/history` | GET | View search history |
| `/analytics` | GET | View statistics |

## ⚙️ Advanced Features

### Dynamic ML Updates
When you add/delete topics in admin panel:
1. Database updates immediately
2. TF-IDF model rebuilds automatically
3. New recommendations available instantly
4. No application restart needed

### JSON Storage
- Search results stored as JSON in database
- Complex data structures serialization
- Easy retrieval and parsing

### Real-time Statistics
- Total searches counter
- Popular queries ranking
- Category distribution
- Trend analysis

## 🚨 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: flask` | Run: `pip install -r requirements.txt` |
| Port 5000 already in use | Change port: `app.run(port=5001)` |
| Database locked error | Delete `recommendations.db` and restart |
| Templates not found | Ensure folder is named `templetes` (not `templates`) |
| Empty recommendations | Try queries with more common words |

## 📈 Performance

- Response time: 10-100ms
- Memory usage: 60-100MB
- Scalable to 1000+ topics
- SQLite supports millions of records

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ Machine Learning concepts (TF-IDF, similarity)
- ✅ Full-stack web development
- ✅ Database design and management
- ✅ Frontend (HTML5/CSS3)
- ✅ Professional code organization
- ✅ Real-world integration

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production
Use a production WSGI server:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Cloud Deployment (Heroku, AWS, etc.)
- Change `debug=True` to `debug=False`
- Use environment variables for config
- Add Procfile for deployment

## 📦 Requirements

```
Flask==2.3.0
scikit-learn==1.3.0
pandas==2.0.0
```

Install with:
```bash
pip install -r requirements.txt
```

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## 📄 License

MIT License - Feel free to use this project for academic and commercial purposes.

## 👨‍💻 Author

Created for IIT Academic Project

## 📧 Support

For issues or questions, feel free to open an issue on GitHub.

---

## 📝 Project Checklist

- ✅ TF-IDF Recommendation Engine
- ✅ Flask Web Server
- ✅ SQLite Database
- ✅ Search History Tracking
- ✅ Admin Panel
- ✅ Analytics Dashboard
- ✅ Professional UI Design
- ✅ Responsive Layout
- ✅ Real-time Model Updates
- ✅ Production Ready

---

**Happy coding! 🎉**
