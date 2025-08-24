# 🏥 DrData - AI-Powered Doctor Analysis Platform

> Smart healthcare data scraping and AI-driven doctor recommendations

![DrData](https://img.shields.io/badge/DrData-v1.0-blue) ![Python](https://img.shields.io/badge/Python-3.11-green) ![AI](https://img.shields.io/badge/AI-Powered-orange)

## ✨ Features

- 🤖 **AI Doctor Analysis** - Smart recommendations based on ratings & experience
- 📊 **Interactive Dashboard** - Beautiful black/white/gray UI with rounded design
- 🔍 **Multi-Source Scraping** - Automated data collection from JustDial
- 📈 **Real-time Insights** - Specialty analysis, location trends, top doctors
- 📱 **Responsive Design** - Works on desktop and mobile
- 🔄 **Auto Updates** - N8N automation for fresh data

## 🚀 Quick Start

### Option 1: Docker (Recommended)
```bash
git clone <your-repo>
cd DrData
docker-compose up -d
```
Open `http://localhost:8000`

### Option 2: Manual Setup
```bash
# Clone and install
git clone <your-repo>
cd DrData
pip install -r requirements.txt

# Run scraper (optional - sample data included)
python multi_healthcare_scraper.py

# Start web server
python -m http.server 8000
```

## 📋 Requirements

- Python 3.11+
- Chrome Browser
- 4GB RAM minimum

## 🛠️ Installation

### Windows
```cmd
pip install -r requirements.txt
python multi_healthcare_scraper.py
```

### Linux/Mac
```bash
sudo apt install python3-pip google-chrome-stable
pip3 install -r requirements.txt
python3 multi_healthcare_scraper.py
```

## 📁 Project Structure

```
DrData/
├── index.html              # Main dashboard
├── multi_healthcare_scraper.py  # Core scraper
├── ai_analyzer.py          # AI analysis engine
├── n8n_automation.py       # Automation script
├── healthcare_doctors.xlsx # Sample data
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## 🎯 Usage

1. **View Dashboard**: Open `index.html` in browser
2. **Select Specialty**: Choose from dropdown for AI recommendations
3. **Analyze Data**: Click buttons for different insights
4. **Update Data**: Run `python n8n_automation.py`

## 🔧 Configuration

Edit specialties in `multi_healthcare_scraper.py`:
```python
specialties = ['Cardiology', 'Dermatology', 'Neurology']
```

## 📊 AI Insights

- **Top Rated Doctors** - Highest patient satisfaction
- **Experience Analysis** - Years of practice statistics  
- **Specialty Breakdown** - Distribution across fields
- **Location Insights** - Geographic analysis
- **Smart Recommendations** - AI scoring (60% rating + 40% experience)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Submit pull request

## 📄 License

MIT License - feel free to use and modify

---
**Made with ❤️ by Aditya Kumar for better healthcare decisions**