# 🚀 Setup Guide - Smart Content Recommendation System

## Prerequisites

- Python 3.9 or higher
- Git (for version control)
- GitHub account

## Step-by-Step Setup

### 1. Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `Smart-Content-Recommendation-System`
3. Add description: "A Flask web application for intelligent content recommendations"
4. Choose Public (for sharing)
5. Click "Create repository"

### 2. Clone to Your Computer

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Content-Recommendation-System.git
cd Smart-Content-Recommendation-System
```

### 3. Setup Virtual Environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

### 6. Open in Browser

- Navigate to: http://127.0.0.1:5000
- Test all features:
  - Search for topics
  - Check history
  - Add/delete topics in admin
  - View analytics

## 📁 File Structure for GitHub

```
Smart-Content-Recommendation-System/
│
├── app.py                    # Main application
├── requirements.txt          # Dependencies
├── README.md                 # Project documentation
├── SETUP.md                  # This file
├── .gitignore               # Git ignore rules
│
├── templetes/               # HTML templates folder
│   ├── index.html           # Search page
│   ├── history.html         # History page
│   ├── admin.html           # Admin panel
│   └── analytics.html       # Analytics dashboard
│
├── .venv/                   # Virtual environment (in .gitignore)
│
└── recommendations.db       # Database (auto-created, in .gitignore)
```

## 📤 Push to GitHub

### First Time

```bash
git add .
git commit -m "Initial commit: Smart Content Recommendation System"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Smart-Content-Recommendation-System.git
git push -u origin main
```

### After Making Changes

```bash
git add .
git commit -m "Description of changes"
git push origin main
```

## ✅ Verification Checklist

- [ ] All files are in the project folder
- [ ] `requirements.txt` has correct dependencies
- [ ] `README.md` is comprehensive
- [ ] `.gitignore` is configured
- [ ] App runs without errors
- [ ] All 4 pages work (Search, History, Admin, Analytics)
- [ ] Repository is on GitHub
- [ ] All files are committed

## 🎯 GitHub Repository URL

After setup, your repository will be at:
```
https://github.com/YOUR_USERNAME/Smart-Content-Recommendation-System
```

Share this link for your project submission!

## 📝 Jupyter Notebook

The Jupyter Notebook (`Smart_Content_Recommendation_System.ipynb`) contains:
- Project overview
- Code explanations
- Demonstrations
- Learning outcomes
- Troubleshooting guide

## 🚀 Deployment Options

### Option 1: Heroku (Free)
```bash
pip install gunicorn
# Create Procfile with: web: gunicorn app:app
git push heroku main
```

### Option 2: AWS/DigitalOcean
- Install on cloud server
- Run with Gunicorn
- Use Nginx as reverse proxy

### Option 3: Docker
Create `Dockerfile` for containerized deployment

## 💡 Tips

- Keep `.venv` folder in `.gitignore` (don't upload)
- Keep `recommendations.db` in `.gitignore` initially
- Add meaningful commit messages
- Update README as you improve the project
- Test before pushing to GitHub

## 🆘 Common Issues

**Issue: File not found in templates**
- Solution: Ensure folder is named `templetes` (with typo)

**Issue: Port 5000 in use**
- Solution: Change `app.run(port=5001)` in app.py

**Issue: Dependencies not installing**
- Solution: Update pip: `pip install --upgrade pip`

## ✨ Next Steps

1. ✅ Download this project folder
2. ✅ Create GitHub repository
3. ✅ Push all files to GitHub
4. ✅ Test the application
5. ✅ Share GitHub link for submission

---

**Ready to submit! Good luck with your project! 🎉**
