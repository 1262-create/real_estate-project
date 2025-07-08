🏠 Real Estate Price Predictor

This project is an end-to-end real estate price prediction web app that estimates property prices based on key features like location, area, number of bedrooms, and more. It also includes an interactive analytics dashboard and a content-based property recommender system.

🚀 Demo
Live App:http://16.171.168.107:8502/

📌 Features
🔮 Price Prediction: Predict apartment prices using a trained XGBoost model with 91% R² score and ₹11L mean absolute error.

📊 Analytics Dashboard: Visualize price distribution, top locations, area trends, word clouds, scatter plots, pie charts, and more.

🧠 Recommender System: Suggests similar properties based on user-selected apartment & geographical radius.

🌐 Deployed on AWS: Fully accessible via public URL.

📦 Modular Codebase: Organized into reusable components using Streamlit pages.

🧠 Model Highlights
Model Used: XGBoost Regressor

Evaluation:

R² Score: 91%

Mean Absolute Error (MAE): ₹11,00,000

Feature Engineering:

Outlier treatment

Missing value imputation

Label encoding & category encoding

Feature selection using correlation, mutual info, and model-based importance

🔍 Data Collection
Data was scraped from 99acres.com using BeautifulSoup and custom web scrapers.

Cleaned and prepared using Pandas and NumPy.

🛠 Tools & Technologies
Category	Tools/Libraries
Programming	Python
Web App Framework	Streamlit
ML Model	XGBoost, scikit-learn
Data Analysis	Pandas, NumPy, Matplotlib, Seaborn
Deployment	AWS EC2
Extras	category_encoders,  Plotly

📁 Directory Structure
bash
Copy
Edit
├── Home.py                # Landing page
├── pages/
│   ├── price_predictor.py # Prediction module
│   ├── analytics.py       # Dashboard visuals
│   └── recommender.py     # Similar property recommender
├── model/
│   └── pipeline.pkl       # Trained XGBoost pipeline
├── data/
│   └── df.pkl # Cleaned dataset
└── utils/                 # Helper functions
