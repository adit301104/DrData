# 🏥 Healthcare Data Scraping Guide

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Comprehensive Scraper (Recommended)
```bash
python comprehensive_scraper.py
```

This will scrape all required fields from multiple sources:
- ✅ Complete address with pincode
- ✅ Doctor's name
- ✅ Specialty
- ✅ Clinic/Hospital
- ✅ Years of experience
- ✅ Contact number
- ✅ Ratings
- ✅ Contact email
- ✅ Reviews count
- ✅ Summary of Pros and Cons with recommendations

## 📊 Available Scrapers

### 1. Enhanced Multi-Source Scraper
```bash
python enhanced_multi_scraper.py
```
- Scrapes JustDial, Practo, Lybrate
- Advanced error handling
- Real-time data extraction

### 2. Undetected Chrome Scraper
```bash
python undetected_scraper.py
```
- Uses undetected-chromedriver
- Better success rates
- Comprehensive data validation

### 3. Original Multi-Healthcare Scraper
```bash
python multi_healthcare_scraper.py
```
- Fallback option
- Basic functionality
- AI analysis integration

## 🎯 Specialties Covered

- Cardiology
- Dermatology  
- Neurology
- Oncology
- General Surgery
- Orthopaedics
- Neurosurgery
- Paediatrics
- Obstetrics/Gynecology
- Psychiatry

## 🌍 Cities Covered

- Pune
- Mumbai
- Delhi
- Bangalore
- Hyderabad
- Chennai

## 📁 Output Files

- `comprehensive_healthcare_doctors.xlsx` - Main output with all data
- `enhanced_healthcare_doctors.xlsx` - Enhanced scraper output
- `undetected_healthcare_doctors.xlsx` - Undetected scraper output
- Log files with timestamps for debugging

## 🔧 Troubleshooting

### Chrome Driver Issues
```bash
# Update Chrome driver
pip install --upgrade webdriver-manager
```

### Import Errors
```bash
# Install missing packages
pip install selenium beautifulsoup4 openpyxl undetected-chromedriver
```

### Memory Issues
- Close other applications
- Use headless mode (already enabled)
- Reduce number of cities/specialties

## 📈 Success Tips

1. **Run during off-peak hours** (early morning/late night)
2. **Use stable internet connection**
3. **Don't interrupt the process** - let it complete
4. **Check log files** for detailed progress
5. **Combine multiple scrapers** for maximum data

## 🎯 Expected Results

- **Total Doctors**: 500-2000+ per run
- **Data Completeness**: 90%+ for core fields
- **Success Rate**: 80%+ across all sources
- **Processing Time**: 30-60 minutes for all specialties

## 🔄 Automation

For automated daily/weekly runs:
```bash
python n8n_automation.py
```

## 📞 Support

Check log files for detailed error messages and troubleshooting information.