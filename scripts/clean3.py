import os
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

df = pd.read_csv("../data/IDS_CountryMetaData.csv", encoding="cp1252")
# Basic analysis of the dataset
print("Dataset shape:", df.shape)
print("Columns:", df.columns)   
print(df.info())

# Check for missing values
missing = df.isnull().sum()
missing_percent = (missing / len(df)) * 100
missing_df = pd.DataFrame({
    "Missing Values": missing,
    "Percentage": missing_percent
})
print(missing_df.sort_values(by="Percentage", ascending=False))

# remove duplicates
print(df.duplicated().sum())
# duplicate country codes
print(df["Code"].duplicated().sum())
# unique country codes
print(df["Code"].nunique())
# check for blank strings 
for col in df.select_dtypes(include=['object', 'string']).columns:
    blanks = (df[col].str.strip() == "").sum()
    if blanks > 0:
        print(col, blanks)
# standardize column names
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
      .str.replace("-", "_")
)
# remove leading and trailing spaces
text_cols = df.select_dtypes(include=["object", "string"]).columns
for col in text_cols:
    df[col] = df[col].str.strip()

# Final validation of the dataset
print("=" * 50)
print("DATA VALIDATION REPORT")
print("=" * 50)
print(f"Shape               : {df.shape}")
print(f"Duplicate Rows      : {df.duplicated().sum()}")
print(f"Duplicate Codes     : {df['code'].duplicated().sum()}")
print(f"Unique Country Codes: {df['code'].nunique()}")
print("\nMissing Values")
print(df.isnull().sum())
print("\nData Types")
print(df.dtypes)
print("=" * 50)
print("Dataset Validation Completed")

# Save the cleaned dataset
df.to_csv("../data/IDS_CountryMetaData_cleaned.csv", index=False)
print(" Cleaned dataset saved successfully!")
# reorder columns for better readability
first_cols = [
    "code",
    "long_name",
    "short_name",
    "region",
    "income_group",
    "lending_category"
]
remaining_cols = [col for col in df.columns if col not in first_cols]
df = df[first_cols + remaining_cols]

# EDA
# =====================================================================
# EXPLORATORY DATA ANALYSIS (EDA)
# =====================================================================
print("=== CATEGORICAL DISTRIBUTIONS ===")
print("\n[Income Groups]\n", df["income_group"].value_counts())
print("\n[Geographic Regions]\n", df["region"].value_counts())
print("\n[Lending Categories]\n", df["lending_category"].value_counts())
print("\n[External Debt Reporting Status]\n", df["external_debt_reporting_status"].value_counts())
print("\n[Currency Unit Summary (Top 5)]\n", df["currency_unit"].value_counts().head(5))

print("\n=== MACRO STRUCTURAL CROSS-TABS ===")
print("\n[Region vs Income Group]")
print(pd.crosstab(df["region"], df["income_group"]))

print("\n[Region vs Lending Category]")
print(pd.crosstab(df["region"], df["lending_category"]))

# 5. Corelation Matrix Visual Focus
numeric_df = df.select_dtypes(include="number")
if not numeric_df.empty and numeric_df.shape[1] > 1:
    plt.figure(figsize=(8, 6))
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1)
    plt.title("Correlation Matrix of Reference Year Metrics")
    plt.tight_layout()
    plt.savefig("numeric_correlation_matrix.png")
    plt.close()
    print("\n📈 Correlation heatmap saved as 'numeric_correlation_matrix.png'")

# Metadata Completeness Tracking Metric
df["non_null_fields"] = df.notnull().sum(axis=1)
print("\n=== TOP 5 MOST COMPLETE RECORDS ===")
print(df[["code", "long_name", "non_null_fields"]].sort_values(by="non_null_fields", ascending=False).head(5))