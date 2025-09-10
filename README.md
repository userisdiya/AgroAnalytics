# AgroAnalytics
AgroAnalytics is an intelligent web-based crop recommendation system that helps farmers make data-driven decisions about which crops to plant based on soil conditions, weather data, and environmental factors.

## 🚀 Features

### 🔐 Authentication System
- *User Registration & Login*: Secure user authentication with session management
- *Profile Management*: Users can view and edit their personal information
- *Session Security*: Auto-redirect logged-in users, secure logout functionality
- *Responsive Navigation*: Professional navbar with user profile dropdown

### 🧠 Machine Learning Powered Predictions
- *Smart Crop Recommendations*: Uses Random Forest Classifier trained on 2,200+ data points
- *22 Crop Types Supported*: Rice, Maize, Chickpea, Kidney beans, Pigeon peas, Moth beans, Mung bean, Black gram, Lentil, Pomegranate, Banana, Mango, Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, Coconut, Cotton, Jute, Coffee
- *High Accuracy*: Model accuracy typically >95%
- *Confidence Scoring*: Provides confidence percentage for each recommendation
- *Top 5 Predictions*: Shows ranked list of suitable crops with probabilities

### 🌤️ Real-time Weather Integration
- *OpenWeatherMap API*: Fetches live weather data for any Indian city
- *Comprehensive Weather Data*: Temperature, humidity, rainfall estimation
- *Smart Rainfall Estimation*: Converts current weather conditions to seasonal rainfall patterns
- *Location Intelligence*: Supports 100+ Indian cities including major agricultural centers

### 📊 Data Visualization
- *Interactive Charts*: Bar graphs showing crop recommendation probabilities
- *Detailed Reports*: Complete input parameters and weather source information
- *User-friendly Interface*: Clean, responsive design with agricultural theme

### 🌐 User Experience
- *Intuitive Interface*: Easy-to-use forms with comprehensive city selection
- *Responsive Design*: Works seamlessly on desktop, tablet, and mobile devices
- *Real-time Feedback*: Loading indicators and error handling
- *Agricultural Focus*: Specialized city database including farming regions

## 🛠️ Technology Stack

### Backend
- *Framework*: Django 5.2.4
- *Database*: SQLite3 (Development)
- *Machine Learning*: scikit-learn 1.7.1
- *Data Processing*: pandas 2.3.1, NumPy 2.3.2
- *Visualization*: matplotlib 3.10.5
- *HTTP Requests*: requests 2.32.4

### Frontend
- *Template Engine*: Django Templates
- *Styling*: Custom CSS with responsive design
- *JavaScript*: Vanilla JS for form handling
- *UI Framework*: Custom green agricultural theme

### APIs & Services
- *Weather Data*: OpenWeatherMap API
- *Geocoding*: OpenWeatherMap Geocoding API

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- OpenWeatherMap API key (free registration required)

## ⚡ Quick Start

### 1. Clone the Repository
bash
git clone https://github.com/nerdyADITYA/Agro_Analytics.git
cd AgroAnalytics


### 2. Create Virtual Environment
bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate


### 3. Install Dependencies
bash
pip install django==5.2.4 scikit-learn==1.7.1 pandas==2.3.1 matplotlib==3.10.5 requests==2.32.4 numpy==2.3.2


Or install all at once:
bash
pip install django scikit-learn pandas matplotlib requests numpy


### 4. Configure API Key
1. Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api)
2. Replace the API key in Crop/views.py line 101:
python
api_key = 'your_api_key_here'


### 5. Run Migrations
bash
python manage.py migrate


### 6. Start Development Server
bash
python manage.py runserver


### 7. Access the Application
Open your browser and navigate to http://127.0.0.1:8000/

## 📖 Usage Guide

### Getting Started
1. *Sign Up*: Create a new account with your details
2. *Login*: Access the system with your credentials
3. *Input Data*: Fill in soil parameters (N, P, K, pH) and select your city
4. *Get Recommendations*: Click "Predict Best Crop" to get AI-powered suggestions
5. *Analyze Results*: Review the recommended crops with confidence scores and charts

### Input Parameters
- *Nitrogen (N)*: Nitrogen content in soil (0-140 range typical)
- *Phosphorus (P)*: Phosphorus content in soil (5-145 range typical)
- *Potassium (K)*: Potassium content in soil (5-205 range typical)
- *pH Value*: Soil acidity/alkalinity (3.0-10.0 range, 6.0-7.5 optimal for most crops)
- *City*: Select from 100+ Indian cities for weather data

### Understanding Results
- *Primary Recommendation*: The crop with highest probability
- *Confidence Score*: Percentage indicating model certainty
- *Top 5 Crops*: Ranked list of suitable alternatives
- *Visual Chart*: Bar graph showing probability distribution
- *Environmental Data*: Weather conditions used in prediction

## 🗂️ Project Structure


AgroAnalytics/
├── AgroAnalytics/          # Main project settings
│   ├── __init__.py
│   ├── settings.py         # Django configuration
│   ├── urls.py            # Main URL routing
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── Crop/                   # Main application
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
│   │   ├── home.html      # Main prediction interface
│   │   ├── login.html     # User authentication
│   │   ├── signup.html    # User registration
│   │   └── profile.html   # User profile management
│   ├── models.py          # Database models (User, Crop)
│   ├── views.py           # Application logic and ML pipeline
│   ├── urls.py            # App URL routing
│   ├── admin.py           # Django admin configuration
│   ├── apps.py            # App configuration
│   ├── tests.py           # Unit tests
│   └── Crop_recommendation.csv  # Training dataset (2200+ records)
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
└── README.md              # Project documentation


## 🧮 Machine Learning Model

### Algorithm: Random Forest Classifier
- *Training Data*: 2,200 samples across 22 crop types
- *Features*: 7 input parameters (N, P, K, temperature, humidity, pH, rainfall)
- *Model Performance*: Typically >95% accuracy
- *Cross-validation*: 80/20 train-test split

### Feature Engineering
- *Soil Chemistry*: NPK values and pH levels
- *Climate Data*: Temperature and humidity from weather API
- *Rainfall Estimation*: Smart conversion from current weather to seasonal patterns
- *Feature Scaling*: Automatic handling within scikit-learn pipeline

### Prediction Process
1. *Input Validation*: Ensures all parameters are within valid ranges
2. *Weather Fetching*: Real-time API calls for current conditions
3. *Data Preprocessing*: Formats input for ML model
4. *Prediction*: Random Forest generates probability scores
5. *Post-processing*: Ranks crops and generates visualizations

## 🌾 Supported Crops

| Cereal Crops | Legume Crops | Fruit Crops | Cash Crops |
|--------------|--------------|-------------|------------|
| Rice | Chickpea | Banana | Cotton |
| Maize | Kidney beans | Mango | Jute |
| | Pigeon peas | Grapes | Coffee |
| | Moth beans | Watermelon | |
| | Mung bean | Muskmelon | |
| | Black gram | Apple | |
| | Lentil | Orange | |
| | | Papaya | |
| | | Coconut | |
| | | Pomegranate | |

## 🌍 Weather Data Coverage

### City Categories
- *Major Cities*: Mumbai, Delhi, Bangalore, Hyderabad, Chennai, Kolkata, Pune
- *State Capitals*: All Indian state capitals included
- *Agricultural Centers*: Specialized farming regions like Amritsar, Karnal, Sangli
- *Geographic Spread*: 100+ cities across all Indian states

### Weather Parameters
- *Temperature*: Real-time temperature in Celsius
- *Humidity*: Percentage humidity levels
- *Rainfall*: Intelligent estimation based on current weather patterns
- *Location Data*: GPS coordinates for precise weather data

## 🔧 API Endpoints

### Authentication
- GET / - User registration page
- GET /login/ - User login page
- POST /login/ - Process login credentials
- GET /logout/ - User logout

### Core Features
- GET /home/ - Main prediction interface
- POST /home/ - Process crop prediction (via GET parameters)
- GET /profile/ - User profile page
- POST /profile/ - Update user profile

### Data Flow
1. User submits form with soil parameters and city
2. System validates input data
3. Weather API fetched for real-time conditions
4. Machine learning model processes combined data
5. Results generated with visualizations
6. Data stored in database for future reference

## 🔒 Security Features

- *Session Management*: Secure user sessions with Django's built-in system
- *CSRF Protection*: Cross-site request forgery protection on all forms
- *Input Validation*: Server-side validation for all user inputs
- *SQL Injection Prevention*: Django ORM prevents SQL injection attacks
- *XSS Protection*: Template system automatically escapes user content

## 🎨 UI/UX Features

- *Agricultural Theme*: Green color scheme reflecting agricultural focus
- *Responsive Design*: Mobile-friendly interface
- *Intuitive Navigation*: Clear navbar with user profile dropdown
- *Error Handling*: Comprehensive error messages and validation
- *Loading States*: Visual feedback during API calls
- *Accessibility*: Semantic HTML and proper form labels

## 🧪 Testing

Run the test suite:
bash
python manage.py test


## 📊 Database Schema

### User Model
python
class User(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Username = models.CharField(max_length=100, unique=True)
    Email = models.EmailField(max_length=100, unique=True)
    Age = models.IntegerField()
    Phone_Number = models.CharField(max_length=15, unique=True)
    Password = models.CharField(max_length=100)


### Crop Model
python
class Crop(models.Model):
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    temprature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()


## 🚀 Deployment

### Production Considerations
1. *Environment Variables*: Store API keys in environment variables
2. *Database*: Switch to PostgreSQL or MySQL for production
3. *Static Files*: Configure proper static file handling
4. *Security Settings*: Set DEBUG=False, configure ALLOWED_HOSTS
5. *HTTPS*: Enable SSL/TLS encryption
6. *Caching*: Implement Redis or Memcached for better performance

### Deployment Platforms
- *Heroku*: Easy deployment with Git integration
- *PythonAnywhere*: Python-focused hosting platform
- *DigitalOcean*: VPS with full control
- *AWS*: Enterprise-scale cloud deployment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (git checkout -b feature/new-feature)
3. Commit changes (git commit -am 'Add new feature')
4. Push to branch (git push origin feature/new-feature)
5. Create Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comprehensive docstrings
- Write unit tests for new features
- Update documentation for API changes

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- *Dataset*: Crop recommendation dataset from agricultural research
- *Weather API*: OpenWeatherMap for reliable weather data
- *ML Framework*: scikit-learn community for excellent documentation
- *Django Community*: For the robust web framework

## 📞 Support

For support, feature requests, or bug reports:
- Create an issue on GitHub
- Contact: [userisdiya](https://github.com/userisdiya)

## 🔮 Future Enhancements

- *Mobile App*: React Native or Flutter mobile application
- *Advanced ML*: Deep learning models for improved accuracy
- *Soil Testing*: Integration with IoT soil sensors
- *Market Prices*: Real-time crop price integration
- *Multilingual*: Support for regional languages
- *Weather Forecasting*: Extended weather predictions
- *Crop Calendar*: Seasonal planting recommendations
- *Yield Prediction*: Estimated crop yield calculations

---

*Built with ❤️ for farmers and agriculture enthusiasts*