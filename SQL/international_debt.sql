-- 1. `public.countries`
-- Matches all columns in `IDS_CountryMetaData_cleaned.csv`.
-- =========================================================================
CREATE TABLE public.countries (
    country_code VARCHAR(10) PRIMARY KEY, -- maps to 'code' in CSV
    long_name TEXT,
    income_group TEXT,
    region TEXT,
    lending_category TEXT,
    other_groups TEXT,
    currency_unit TEXT,
    latest_population_census TEXT,
    latest_household_survey TEXT,
    special_notes TEXT,
    national_accounts_base_year TEXT,
    national_accounts_reference_year TEXT,
    system_of_national_accounts TEXT,
    sna_price_valuation TEXT,
    ppp_survey_years TEXT,
    balance_of_payments_manual_in_use TEXT,
    external_debt_reporting_status TEXT,
    system_of_trade TEXT,
    government_accounting_concept TEXT,
    imf_data_dissemination_standard TEXT,
    source_of_most_recent_income_and_expenditure_data TEXT,
    vital_registration_complete TEXT,
    latest_agricultural_census TEXT,
    latest_industrial_data TEXT,
    latest_trade_data TEXT,
    latest_water_withdrawal_data TEXT,
    two_alpha_code TEXT,                  -- maps to '2_alpha_code' in CSV
    wb_2_code TEXT,
    table_name TEXT,
    short_name TEXT
);

-- =========================================================================
-- 2. `public.indicators`
-- Matches all columns in `IDS_SeriesMetaData_cleaned.csv`.
-- =========================================================================
CREATE TABLE public.indicators (
    indicator_code VARCHAR(50) PRIMARY KEY, -- maps to 'code' in CSV
    indicator_name TEXT,
    topic TEXT,
    source TEXT,
    periodicity TEXT,
    aggregation_method TEXT
);

-- =========================================================================
-- 3. `public.debt_data`
-- The main table for your 143MB dataset.
-- Foreign keys are intentionally flexible to allow import, to be updated later.
-- =========================================================================
CREATE TABLE public.debt_data (
    country_name TEXT NOT NULL,
    country_code TEXT, -- Removed FK constraint for safe import, update and reinforce later.
    indicator_name TEXT NOT NULL,
    indicator_code TEXT, -- Removed FK constraint for safe import, update and reinforce later.
    year INT NOT NULL,
    debt_value NUMERIC(25, 4),
    -- Essential key ensuring each data point is unique by country, indicator, and year.
    PRIMARY KEY (country_name, indicator_name, year)
);

-- =========================================================================
-- 4. `public.country_series_metadata`
-- Matches all columns in `country_series_metadata_cleaned.csv`.
-- Crucially, it does NOT contain the 'id SERIAL' column.
-- =========================================================================
CREATE TABLE public.country_series_metadata (
    type TEXT,
    country_code TEXT,
    country_name TEXT,
    country_short_code TEXT, -- Wide type to allow all content to import.
    series_code TEXT,
    indicator_name TEXT,
    indicator_code TEXT, -- Wide type to allow all content to import.
    description TEXT
);

-- =========================================================================
-- 5. `public.footnotes_country_context`
-- Matches all columns in `IDS_FootNoteMetaData_cleaned.csv`.
-- =========================================================================
CREATE TABLE public.footnotes_country_context (
    country_code VARCHAR(10) PRIMARY KEY, -- maps to 'Code' in CSV
    long_name TEXT,
    income_group TEXT,
    region TEXT,
    lending_category TEXT,
    other_groups TEXT,
    currency_unit TEXT,
    latest_population_census TEXT,
    latest_household_survey TEXT,
    special_notes TEXT,
    national_accounts_base_year TEXT,
    national_accounts_reference_year TEXT,
    system_of_national_accounts TEXT,
    sna_price_valuation TEXT,
    ppp_survey_years TEXT,
    balance_of_payments_manual_in_use TEXT,
    external_debt_reporting_status TEXT,
    system_of_trade TEXT,
    government_accounting_concept TEXT,
    imf_data_dissemination_standard TEXT,
    source_of_most_recent_income_and_expenditure_data TEXT,
    vital_registration_complete TEXT,
    latest_agricultural_census TEXT,
    latest_industrial_data TEXT,
    latest_trade_data TEXT,
    latest_water_withdrawal_data TEXT,
    two_alpha_code TEXT,                  -- maps to '2-alpha code' in CSV
    wb_2_code TEXT,                       -- maps to 'WB-2 code' in CSV
    table_name TEXT,
    short_name TEXT
);

-- =========================================================================
-- Performance Indexes for `debt_data`.
-- Essential for fast queries on your 143MB dataset.
-- =========================================================================
CREATE INDEX idx_debt_year ON public.debt_data(year);
CREATE INDEX idx_debt_country ON public.debt_data(country_name);
CREATE INDEX idx_debt_indicator ON public.debt_data(indicator_name);

-- TOP 20 COUNTRIES BY TOTAL DEBT 
SELECT
    country_name,
    SUM(debt_value) AS total_debt
FROM debt_data
GROUP BY country_name
ORDER BY total_debt DESC
LIMIT 20;

-- LOWEST DEBT 
SELECT
    country_name,
    SUM(debt_value) AS total_debt
FROM debt_data
GROUP BY country_name
ORDER BY total_debt ASC
LIMIT 10;

--Basic Queries
--1)Retrieve all distinct country names from the dataset.
SELECT DISTINCT country_name 
FROM public.debt_data
ORDER BY country_name;
SELECT * FROM public.debt_data;
SELECT * FROM public.countries;
SELECT * FROM public.country_series_metadata;
SELECT * FROM public.footnotes_country_context;
SELECT * FROM public.indicators;

--2)Count the total number of countries available.
SELECT COUNT(country_code) AS total_countries
FROM public.countries;
 
--3)Find the total number of indicators present.
SELECT COUNT(indicator_code) AS total_indicators
FROM public.indicators;

--4)Display the first 10 records of the dataset.
SELECT country_name,country_code,indicator_name,indicator_code,year,debt_value
FROM public.debt_data
LIMIT 10;

--5)Calculate the total global debt.
SELECT SUM(debt_value) AS total_debt 
FROM public.debt_data;

--6)List all unique indicator names.
SELECT DISTINCT(indicator_name) 
FROM public.indicators
ORDER BY indicator_name;

--7)Find the number of records for each country.
SELECT country_name, COUNT(*) as total_record
FROM public.debt_data
GROUP BY country_name
ORDER BY total_record DESC;

--8)Display all records where debt is greater than 1 billion USD.
SELECT * 
FROM public.debt_data
WHERE debt_value > 1000000000;

--9)Find the minimum, maximum, and average debt values.
SELECT 
    MIN(debt_value) AS min_debt, 
    MAX(debt_value) AS max_debt, 
    AVG(debt_value) AS avg_debt
FROM public.debt_data
WHERE debt_value IS NOT NULL;
--10)Count total number of records in the dataset.
SELECT COUNT(*) AS total_records 
FROM public.debt_data;

UPDATE debt_data
SET country_code = TRIM(country_code);

UPDATE countries
SET country_code = TRIM(country_code);

-- QUERY 
SELECT country_code, country_name
FROM debt_data
WHERE country_code = 'ALB';

SELECT country_code, long_name
FROM countries
WHERE country_code = 'ALB';

SELECT LENGTH(country_code), country_code
FROM debt_data
WHERE country_code = 'ALB';

SELECT LENGTH(country_code), country_code
FROM countries
WHERE country_code = 'ALB';

SELECT DISTINCT country_code, country_name
FROM debt_data
WHERE country_name ILIKE '%Alban%';

SELECT DISTINCT country_code
FROM debt_data
ORDER BY country_code
LIMIT 30;

SELECT DISTINCT country_code
FROM debt_data
LIMIT 10;

SELECT 
    c.long_name AS country_name,
    c.region,
    c.income_group,
    SUM(d.debt_value) AS total_debt_usd
FROM public.debt_data d
JOIN public.countries c ON d.country_code = c.country_code
WHERE c.region IS NOT NULL AND c.region <> '' -- Excludes global/regional aggregates
GROUP BY c.long_name, c.region, c.income_group
ORDER BY total_debt_usd DESC
LIMIT 10;