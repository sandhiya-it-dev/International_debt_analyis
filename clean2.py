import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)
# load the CSV file into a DataFrame
df = pd.read_csv("../data/IDS_ALLCountries_Data.csv", encoding="latin1")

# Display first 5 rows
df.head()
print(df.head())
## inspect the dataset
print(df.shape)
print(df.columns)
df.info()
#Remove rows with missing country or indicator information
df = df.dropna(
    subset=[
        "Country Name",
        "Country Code",
        "Series Name",
        "Series Code"
    ]
)
print(df.shape)
# check for duplicates
print("Duplicate rows:", df.duplicated().sum())
# rename columns for consistency
df.rename(columns={
    "Series Name": "Indicator Name",
    "Series Code": "Indicator Code"
}, inplace=True)
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)
print(df.columns)
# Filter Relevant Columns
year_cols = df.columns[6:]

df = df[
    [
        "country_name",
        "country_code",
        "indicator_name",
        "indicator_code"
    ] + list(year_cols)
]

print(df.head())
print(df.shape)

# Convert wide format to long format
year_cols = df.columns[4:]   # After filtering, years start from column index 4

df_long = df.melt(
    id_vars=[
        "country_name",
        "country_code",
        "indicator_name",
        "indicator_code"
    ],
    value_vars=year_cols,
    var_name="year",
    value_name="debt_value"
)

# Remove rows where debt_value is missing
df_long = df_long.dropna(subset=["debt_value"])

# Convert year to integer
df_long["year"] = df_long["year"].astype(int)

print(df_long.head())
print(df_long.shape)

# verifying if no missing values remain
print(df_long.isnull().sum())

df_long.to_csv("../data/IDS_ALLCountries_Data_cleaned.csv", index=False)
print("Cleaned dataset saved successfully!")

# EDA 
df = pd.read_csv("../data/IDS_ALLCountries_Data_cleaned.csv")

# DATA SET OVERVIEW(CLEANED)
print(df_long.shape)
print(df_long.head())
print(df_long.info())

# STATISTICAL SUMMARY
print(df_long.describe())

#Observations
#The dataset covers the years 2000 to 2032.
#Debt values vary over a very wide range, from negative values to extremely large positive values.
#The maximum debt value is 38.2 trillion, indicating some countries or indicators have very high values.
#The mean is much larger than the median, which suggests the data is right-skewed (a few very large values pull the average upward).
#The presence of negative debt values is expected for some indicators (such as net flows or repayments), so you should not remove them without understanding the indicator.

# removing aggregate regions from the dataset to focus on individual countries
aggregates = [
    "High income",
    "Low income",
    "Middle income",
    "Lower middle income",
    "Upper middle income",
    "Low & middle income",

    "IDA total",
    "IDA only",
    "IDA blend",

    "Least developed countries: UN classification",

    "East Asia & Pacific (excluding high income)",
    "Europe & Central Asia (excluding high income)",
    "Latin America & Caribbean (excluding high income)",
    "Middle East & North Africa (excluding high income)",
    "Middle East, North Africa, Afghanistan & Pakistan (excluding high income)",
    "South Asia",
    "Sub-Saharan Africa (excluding high income)"
]
df_long = df_long[~df_long["country_name"].isin(aggregates)]
# COUNTRY ANALYSIS
print("Number of Countries:", df_long["country_name"].nunique())
print(df_long["country_name"].value_counts().head(10))

# Indicator Analysis
for indicator in sorted(df_long["indicator_name"].unique()):
    print(indicator)
# Filtering indicators related to debt
debt_df = df_long[
    df_long["indicator_name"] == "External debt stocks, total (DOD, current US$)"
]

print(debt_df.head())
print(debt_df.shape)

# Country-wise debt distribution
country_debt = debt_df.groupby("country_name")["debt_value"].sum().sort_values(ascending=False)

print(country_debt.head(10))

#Top 10 countries with highest debt
top10 = country_debt.head(10)
print(top10)

#Top 10 countries with lowest debt
bottom10 = country_debt.tail(10)
print(bottom10)

#Year-wise debt trend
yearly_debt = debt_df.groupby("year")["debt_value"].sum()
print(yearly_debt)

# Country trend analysis for a specific country, e.g., India
india = debt_df[debt_df["country_name"] == "India"]
print(india[["year", "debt_value"]])

# =====================================================================
# VISUALIZATION EXTENSIONS
# =====================================================================
sns.set_theme(style="whitegrid")

# Graph A: Top 10 Heavily Indebted Sovereign Nations
plt.figure(figsize=(12, 6))
sns.barplot(
    x=top10.values / 1e9,  # Convert values to Billions for clean presentation
    y=top10.index,
    palette="Reds_r"
)
plt.title("Top 10 Countries with Highest Cumulative External Debt Stocks (Billions USD)")
plt.xlabel("Total Debt Value (Billions USD)")
plt.ylabel("Country Name")
plt.tight_layout()
plt.savefig("top_10_highest_debt_countries.png")
plt.close()

# Graph B: Global Year-over-Year Macro Debt Accumulation Trend
plt.figure(figsize=(12, 5))
sns.lineplot(
    x=yearly_debt.index, 
    y=yearly_debt.values / 1e12,  # Convert to Trillions
    marker="o", 
    color="darkblue", 
    linewidth=2.5
)
plt.title("Global Macro External Debt Accumulation Trend Line (2000 - 2032)")
plt.xlabel("Year")
plt.ylabel("Total Debt Volume (Trillions USD)")
plt.tight_layout()
plt.savefig("global_debt_trend_timeline.png")
plt.close()

print("\n📈 Visualizations successfully generated and saved to your directory!")