�� International Debt Analytics Dashboard
An end-to-end data analytics project that analyzes international debt statistics using Python, Pandas,
PostgreSQL, SQL, and Streamlit. The project includes data cleaning, exploratory data analysis (EDA),
database integration, SQL querying, and an interactive dashboard for visualizing global debt trends.

�� Project Overview
This project processes multiple International Debt Statistics datasets, cleans and transforms the data,
stores it in a PostgreSQL database, and presents insights through an interactive Streamlit dashboard.
The dashboard enables users to:
 Analyze country-wise debt distribution
 Identify countries with the highest and lowest debt
 Explore debt indicators
 Visualize debt trends and patterns
 Filter and interact with the data dynamically

�� Folder Structure
INTERNATIONAL_DEBT/
├── README.md
├── .gitignore
├── .venv/
├── data/
│ ├── IDS_ALLCountries_Data.csv
│ ├── IDS_ALLCountries_Data_cleaned.csv
│ ├── IDS_CountryMetaData.csv
│ ├── IDS_CountryMetaData_cleaned.csv
│ ├── IDS_SeriesMetaData.csv
│ ├── IDS_SeriesMetaData_cleaned.csv
│ ├── IDS_FootNoteMetaData.csv
│ ├── IDS_FootNoteMetaData_cleaned.csv
│ ├── Country-Series - Metadata.csv
│ └── country_series_metadata_cleaned.csv
├── scripts/
│ ├── clean1.py
│ ├── clean2.py
│ ├── clean3.py
│ ├── clean4.py
│ └── clean5.py
├── sql/
│ └── international_debt.sql
└── streamlit_dashboard/
├── app.py
├── database.py
├── requirements.txt
├── .env
├── utils/
└── __pycache__/

�� Project Workflow
1. Data Collection
 Imported multiple International Debt Statistics datasets.
 Included country-level, series-level, and metadata files.
2. Data Cleaning &amp; Preprocessing

The datasets were cleaned using five Python scripts. Cleaning steps included:
 Handling missing values
 Removing duplicate records
 Data type conversion
 Standardizing column names
 Validating and cleaning datasets
 Exporting cleaned CSV files

3. Exploratory Data Analysis (EDA)
Performed EDA to:
 Analyze debt distribution by country
 Identify highest and lowest debt countries
 Explore debt indicators
 Generate descriptive statistics
 Discover trends and patterns

4. PostgreSQL Database Integration
 Created database tables
 Imported cleaned datasets
 Executed SQL queries for analysis
 Connected the dashboard using SQLAlchemy

5. Dashboard Development
Developed an interactive Streamlit dashboard with:
 Dynamic filters
 Interactive Plotly charts
 Country-wise analysis
 Indicator-wise analysis
 Debt trend visualization

✨ Features
 Data cleaning using Pandas
 Exploratory Data Analysis (EDA)
 PostgreSQL database integration
 SQL-based analysis

 Interactive Streamlit dashboard
 Dynamic filtering
 Interactive Plotly visualizations
 Country and indicator analysis


��️ Technologies Used
 Language: Python, SQL
 Data Libraries: Pandas, SQLAlchemy
 Database: PostgreSQL
 Visualization: Plotly Express, Matplotlib, Seaborn
 Framework: Streamlit


�� Installation &amp; Setup
1. Clone the Repository
git clone &lt;repository-url&gt;
cd INTERNATIONAL_DEBT

2. Set Up Virtual Environment
python -m venv .venv

3. Activate Virtual Environment
Windows:
.venv\Scripts\activate
Mac/Linux:
source .venv/bin/activate

4. Install Dependencies
python3 -m pip install -r streamlit_dashboard/requirements.txt

5. Configure Environment Variables
Create a .env file inside the streamlit_dashboard/ directory and configure your server credentials:
DB_HOST=localhost
DB_PORT=5432
DB_NAME=international_debt
DB_USER=your_username

DB_PASSWORD=your_password

6. Run the Application
cd streamlit_dashboard
streamlit run app.py

�� Dashboard Insights
The analytical views provide visual layouts for tracking:
 Country-wise debt distribution
 Top countries with the highest/lowest debt metrics
 Indicator-wise macroeconomic debt analysis
 Timeline debt trend tracking
 Interactive sidebar filtering
�� Future Enhancements
 Add machine learning-based debt forecasting models
 Deploy the live dashboard platform to Streamlit Cloud
 Implement reporting tools to export views as PDF/Excel packages
 Refine framework responsiveness and user session validation

�� Dataset
This project implements historical data tracking derived from the open-source World Bank International
Debt Statistics (IDS) ecosystem alongside relevant relational metadata series.

��‍�� Author: Sandhiya Chandrasekar
Data Analyst | Python | SQL | PostgreSQL | Streamlit | Power BI | Machine Learning