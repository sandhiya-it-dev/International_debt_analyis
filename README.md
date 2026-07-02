# 🌍 International Debt Analytics Dashboard

An end-to-end data analytics project that analyzes international debt statistics using Python, Pandas, PostgreSQL, SQL, and Streamlit. The project includes data cleaning, exploratory data analysis (EDA), database integration, SQL querying, and an interactive dashboard for visualizing global debt trends.

---

## 📌 Project Overview

This project processes multiple International Debt Statistics datasets, cleans and transforms the data, stores it in a PostgreSQL database, and presents insights through an interactive Streamlit dashboard.

The dashboard enables users to:
* Analyze country-wise debt distribution
* Identify countries with the highest and lowest debt
* Explore debt indicators
* Visualize debt trends and patterns
* Filter and interact with the data dynamically

---

## 📂 Folder Structure

```text
INTERNATIONAL_DEBT/
├── README.md
├── .gitignore
├── .venv/
├── data/
│   ├── IDS_ALLCountries_Data.csv
│   ├── IDS_ALLCountries_Data_cleaned.csv
│   ├── IDS_CountryMetaData.csv
│   ├── IDS_CountryMetaData_cleaned.csv
│   ├── IDS_SeriesMetaData.csv
│   ├── IDS_SeriesMetaData_cleaned.csv
│   ├── IDS_FootNoteMetaData.csv
│   ├── IDS_FootNoteMetaData_cleaned.csv
│   ├── Country-Series - Metadata.csv
│   └── country_series_metadata_cleaned.csv
├── scripts/
│   ├── clean1.py
│   ├── clean2.py
│   ├── clean3.py
│   ├── clean4.py
│   └── clean5.py
├── sql/
│   └── international_debt.sql
└── streamlit_dashboard/
    ├── app.py
    ├── database.py
    ├── requirements.txt
    ├── .env
    ├── utils/
    └── __pycache__/

    🔄 Project Workflow
1. Data Collection
Imported multiple International Debt Statistics datasets.

Included country-level, series-level, and metadata files.

2. Data Cleaning & Preprocessing
The datasets were cleaned using five Python scripts. Cleaning steps included:

Handling missing values

Removing duplicate records

Data type conversion

Standardizing column names

Validating and cleaning datasets

Exporting cleaned CSV files

3. Exploratory Data Analysis (EDA)
Performed EDA to:

Analyze debt distribution by country

Identify highest and lowest debt countries

Explore debt indicators

Generate descriptive statistics

Discover trends and patterns

4. PostgreSQL Database Integration
Created database tables

Imported cleaned datasets

Executed SQL queries for analysis

Connected the dashboard using SQLAlchemy

5. Dashboard Development
Developed an interactive Streamlit dashboard with:

Dynamic filters

Interactive Plotly charts

Country-wise analysis

Indicator-wise analysis

Debt trend visualization

✨ Features
Data cleaning using Pandas

Exploratory Data Analysis (EDA)

PostgreSQL database integration

SQL-based analysis

Interactive Streamlit dashboard

Dynamic filtering

Interactive Plotly visualizations

Country and indicator analysis

🛠️ Technologies Used
Python

Pandas

PostgreSQL

SQL

SQLAlchemy

Streamlit

Plotly Express

Matplotlib

Seaborn

🚀 Installation & Setup
1. Clone the repository
Bash
git clone <repository-url>
cd INTERNATIONAL_DEBT
2. Create a virtual environment
Bash
python -m venv .venv
3. Activate the virtual environment
Windows:

Bash
.venv\Scripts\activate
Mac/Linux:

Bash
source .venv/bin/activate
4. Install dependencies
Bash
python3 -m pip install -r streamlit_dashboard/requirements.txt
5. Configure environment variables
Create a .env file inside the streamlit_dashboard/ directory and configure your credentials:

Ini, TOML
DB_HOST=localhost
DB_PORT=5432
DB_NAME=international_debt
DB_USER=your_username
DB_PASSWORD=your_password
6. Run the dashboard
Bash
cd streamlit_dashboard
streamlit run app.py
📊 Dashboard Insights
The dashboard provides clear visual layouts for tracking:

Country-wise debt distribution

Top countries with the highest debt

Top countries with the lowest debt

Indicator-wise debt analysis

Debt trend analysis

Interactive filtering

📈 Future Enhancements
Add machine learning-based debt forecasting

Deploy the application to Streamlit Cloud

Export reports as PDF/Excel

Improve dashboard responsiveness

Add user authentication

📚 Dataset
This project uses the World Bank International Debt Statistics (IDS) dataset, along with country, series, and metadata files for comprehensive debt analysis.

👩‍💻 Author
Sandhiya Chandrasekar

Data Analyst | Python | SQL | PostgreSQL | Streamlit | Power BI | Machine Learning