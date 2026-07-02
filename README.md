# International Debt Analytics Dashboard

An end-to-end data analytics project that analyzes international debt statistics using Python, Pandas, PostgreSQL, SQL, and Streamlit. The project includes data cleaning, exploratory data analysis (EDA), database integration, SQL querying, and an interactive dashboard for visualizing global debt trends.

## Project Overview

This project processes multiple International Debt Statistics datasets, cleans and transforms the data, stores it in a PostgreSQL database, and presents insights through an interactive Streamlit dashboard.

The dashboard enables users to:

- Analyze country-wise debt distribution
- Identify countries with the highest and lowest debt
- Explore different debt indicators
- Visualize debt trends and patterns over time
- Filter and interact with the data dynamically

## Folder Structure

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
```

## Project Workflow

### 1. Data Collection

- Imported multiple International Debt Statistics (IDS) datasets.
- Included country-level, series-level, footnote, and metadata files.

### 2. Data Cleaning & Preprocessing

The datasets were cleaned using five Python scripts (`clean1.py` to `clean5.py`). Key steps:

- Handling missing values
- Removing duplicate records
- Performing data type conversions
- Standardizing column names
- Validating and cleaning datasets
- Exporting cleaned CSV files into the `data/` folder

### 3. Exploratory Data Analysis (EDA)

EDA was performed to:

- Analyze debt distribution by country
- Identify countries with the highest and lowest debt
- Explore debt indicators and their impact
- Generate descriptive statistics
- Discover patterns and trends across regions and time

### 4. PostgreSQL Database Integration

- Created database tables using `sql/international_debt.sql`
- Imported cleaned datasets into PostgreSQL
- Executed SQL queries for aggregations and joins
- Connected the dashboard to PostgreSQL using SQLAlchemy in `database.py`

### 5. Dashboard Development

Developed an interactive Streamlit dashboard (`streamlit_dashboard/app.py`) with:

- Dynamic sidebar filters (e.g., region)
- Interactive Plotly charts
- Country-wise debt analysis
- Indicator-wise debt analysis
- Debt trend visualization over time by income group

## Features

- Data cleaning and preprocessing using Pandas
- Exploratory Data Analysis (EDA)
- PostgreSQL database integration
- SQL-based analysis for aggregations and joins
- Interactive Streamlit dashboard
- Dynamic filtering and slicing
- Interactive visualizations using Plotly, Matplotlib, and Seaborn
- Country-wise and indicator-wise insights

## Technologies Used

- **Language:** Python, SQL
- **Data Libraries:** Pandas, SQLAlchemy
- **Database:** PostgreSQL
- **Visualization:** Plotly Express, Matplotlib, Seaborn
- **Framework:** Streamlit
- **Environment Management:** `python-dotenv`, virtualenv

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd INTERNATIONAL_DEBT
```

### 2. Set Up Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

From the project root (or directly inside `streamlit_dashboard/`):

```bash
python -m pip install -r streamlit_dashboard/requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file inside `streamlit_dashboard/` and configure your PostgreSQL credentials:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=international_debt
DB_USER=your_username
DB_PASSWORD=your_password
```

### 6. Run the Application

```bash
cd streamlit_dashboard
streamlit run app.py
```

## Dashboard Insights

The dashboard provides visual insights for:

- Country-wise debt distribution
- Top countries with the highest and lowest debt
- Indicator-wise macroeconomic debt analysis
- Timeline-based debt trend tracking
- Interactive filtering by region and income group

## Future Enhancements

- Add machine learning-based debt forecasting models
- Deploy the dashboard to Streamlit Community Cloud
- Implement reporting tools to export views as PDF/Excel
- Improve responsiveness, UI styling, and session handling

## Dataset

The project uses historical data inspired by the World Bank International Debt Statistics (IDS) datasets, along with associated country, series, and metadata files.

## Author

**Sandhiya Chandrasekar**  
Data Analyst | Python | SQL | PostgreSQL | Streamlit | Power BI | Machine Learning