import os
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)
# Load dataset
df = pd.read_csv("../data/IDS_CountryMetaData.csv", encoding="cp1252")

# Understand structure ,columns and types
print("Columns:", df.columns.tolist())
print(df.dtypes)
print(df.head())

# Data Preprocessing & Cleaning
    # Handle missing values for key categorical columns safely
categorical_cols = ['Income Group', 'Region', 'External debt Reporting status']
for col in categorical_cols:
    if col in df.columns:
        df[col] = df[col].fillna('Unknown')

    # Remove duplicate records based on the primary key 'Code'
    if 'Code' in df.columns:
        df = df.drop_duplicates(subset=['Code'])

    # Filter down to the most relevant columns for debt tracking
    relevant_columns = ['Code', 'Long Name', 'Income Group', 'Region', 'External debt Reporting status', 'Currency Unit']
    # Dynamically select only the relevant columns that actually exist in the file
    columns_to_keep = [col for col in relevant_columns if col in df.columns]
    df_cleaned = df[columns_to_keep].copy()

    # Standardize string data (strip accidental whitespace)
    for col in df_cleaned.select_dtypes(include=['object', 'str']).columns:
        df_cleaned[col] = df_cleaned[col].str.strip()

    print("\n--- Cleaned Dataset Structure ---")
    print(df_cleaned.info())
    print("\nSample Data:")
    print(df_cleaned.head())

# Save the cleaned dataset
df.to_csv("../data/IDS_FootNoteMetaData_cleaned.csv", index=False)
print(" Cleaned dataset saved successfully!")

# EDA 
import matplotlib.pyplot as plt
import seaborn as sns

print("\n=============================================")
print("     EXPLORATORY DATA ANALYSIS (EDA)        ")
print("=============================================\n")

# 1. Calculate Percentages for Key Metrics
print("--- Income Group Proportions ---")
income_pct = df_cleaned['Income Group'].value_counts(normalize=True) * 100
for group, pct in income_pct.items():
    print(f" * {group}: {pct:.1f}%")

print("\n--- Geographic Region Proportions ---")
region_pct = df_cleaned['Region'].value_counts(normalize=True) * 100
for region, pct in region_pct.items():
    print(f" * {region}: {pct:.1f}%")

print("\n--- Debt Reporting Status Proportions ---")
status_pct = df_cleaned['External debt Reporting status'].value_counts(normalize=True) * 100
for status, pct in status_pct.items():
    print(f" * {status}: {pct:.1f}%")

# 2. Visualizing the Distributions
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Chart 1: Income Group Distribution
sns.countplot(
    data=df_cleaned, 
    y='Income Group', 
    hue='Income Group',  # Added hue
    legend=False,        # Removed redundant legend
    ax=axes[0], 
    order=df_cleaned['Income Group'].value_counts().index,
    palette='Blues_r'
)
axes[0].set_title('Distribution of Countries by Income Group')
axes[0].set_xlabel('Number of Countries')

# Chart 2: Geographic Region Distribution
sns.countplot(
    data=df_cleaned, 
    y='Region', 
    hue='Region',        # Added hue
    legend=False,        # Removed redundant legend
    ax=axes[1], 
    order=df_cleaned['Region'].value_counts().index,
    palette='Greens_r'
)
axes[1].set_title('Distribution of Countries by Geographic Region')
axes[1].set_xlabel('Number of Countries')

plt.tight_layout()
plt.savefig('country_metadata_eda.png')
print("\n[Success] EDA Plots saved as 'country_metadata_eda.png'")
plt.show()

