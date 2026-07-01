# International Debt Analytics Dashboard

A Streamlit and PostgreSQL-based data analytics project for exploring international debt statistics through cleaning, database integration, SQL analysis, and interactive visualizations.

## Project Overview

This project analyzes international debt data using multiple raw datasets collected from country, series, and metadata files. The raw files were cleaned using separate Python scripts, transformed into structured datasets, stored in PostgreSQL, and connected to a Streamlit dashboard for visualization and analysis.

The dashboard helps analyze:
- Country-wise debt distribution
- Top countries with highest debt
- Top countries with lowest debt
- Debt distribution across indicators
- Trends and patterns in international debt over time

## Folder Structure

```bash
INTERNATIONAL_DEBT/
│
├── .venv/                              # Virtual environment
├── multi_dataset/                      # Raw and cleaned dataset files
│   ├── clean1.py
│   ├── clean2.py
│   ├── clean3.py
│   ├── clean4.py
│   ├── clean5.py
│   ├── country_series_metadata_cleaned.csv
│   ├── Country-Series - Metadata.csv
│   ├── IDS_ALLCountries_Data_cleaned.csv
│   ├── IDS_ALLCountries_Data.csv
│   ├── IDS_CountryMetaData_cleaned.csv
│   ├── IDS_CountryMetaData.csv
│   ├── IDS_FootNoteMetaData_cleaned.csv
│   ├── IDS_FootNoteMetaData.csv
│   ├── IDS_SeriesMetaData_cleaned.csv
│   ├── IDS_SeriesMetaData.csv
│   └── international_debt.sql         # SQL file for database/table creation
│
├── streamlit_dashboard/                # Dashboard application
│   ├── __pycache__/
│   ├── utils/
│   ├── .env                           # Environment variables
│   ├── app.py                         # Main Streamlit app
│   ├── database.py                    # PostgreSQL connection logic
│   └── requirements.txt               # Python dependencies
```

## Project Workflow

### 1. Data Collection
The project uses multiple international debt-related files, including:
- Country-level data
- Country metadata
- Series metadata
- Footnote metadata
- Country-series metadata

### 2. Data Preprocessing
The following preprocessing steps were completed:
- Handle missing values (null data)
- Remove duplicate records
- Perform data type conversion
- Filter relevant columns such as country, indicators, and debt values
- Standardize and clean the dataset

Five separate cleaning scripts were used:
- `clean1.py`
- `clean2.py`
- `clean3.py`
- `clean4.py`
- `clean5.py`

These scripts cleaned raw CSV files and generated structured cleaned datasets for further analysis.

### 3. Exploratory Data Analysis (EDA)
The following EDA tasks were completed:
- Analyze country-wise debt distribution
- Identify top countries with highest and lowest debt
- Explore different debt indicators and their impact
- Identify patterns, trends, and relationships
- Perform statistical summaries and comparisons

### 4. Database Integration
The cleaned data was loaded into PostgreSQL using the SQL script:
- `international_debt.sql`

The database connection for the dashboard is managed using:
- `database.py`

### 5. Dashboard Development and Visualization
The Streamlit dashboard is created in:
- `app.py`

The dashboard includes visualizations created using:
- Plotly
- Seaborn
- Matplotlib

Visual insights were built for:
- Country-wise debt analysis
- Indicator-wise debt analysis
- Trend analysis over time

The app connects to PostgreSQL, runs SQL queries, applies filters, and displays charts for debt analysis.

## Technologies Used

- Python
- Pandas
- Streamlit
- PostgreSQL
- SQLAlchemy
- Plotly Express
- Matplotlib
- Seaborn

## How to Run the Project

### 1. Open the dashboard folder

```bash
cd streamlit_dashboard
```

### 2. Activate the virtual environment

**Windows**
```bash
.venv\Scripts\activate
```

**Mac/Linux**
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Make sure your `.env` file contains the PostgreSQL database credentials.

Example:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=international_debt
DB_USER=your_username
DB_PASSWORD=your_password
```

### 5. Run the Streamlit application

```bash
streamlit run app.py
```