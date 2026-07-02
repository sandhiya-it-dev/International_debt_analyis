import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================================
# 1. DATA COLLECTION
# =====================================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()
os.chdir(SCRIPT_DIR)

# Load the series metadata file explicitly 
df_series = pd.read_csv("../data/IDS_SeriesMetaData.csv", encoding="latin1")

print("=== 1. INITIAL DATA PROFILE ===")
print(f"Dataset Shape: {df_series.shape}")
print(f"Columns: {list(df_series.columns)}")
print("\n--- Initial Column Types & Non-Null Counts ---")
print(df_series.info())

# =====================================================================
# 2. DATA PREPROCESSING
# =====================================================================
# Remove duplicate records
initial_rows = len(df_series)
df_series = df_series.drop_duplicates()
print(f"\nRemoved {initial_rows - len(df_series)} duplicate rows.")

# Standardize and clean column headers into snake_case
df_series.columns = (
    df_series.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_", regex=False)
      .str.replace("-", "_", regex=False)
)

# Standardize text data and handle missing strings cleanly
text_cols = df_series.select_dtypes(include=["object", "string", "str"]).columns
for col in text_cols:
    df_series[col] = df_series[col].str.strip()

# Explicit type conversion to maintain safe categorical segments
df_series["code"] = df_series["code"].astype("string")
df_series["indicator_name"] = df_series["indicator_name"].astype("string")
df_series["topic"] = df_series["topic"].astype("category")

# Filtering relevant structural columns
relevant_cols = ["code", "indicator_name", "topic", "source", "periodicity", "aggregation_method"]
df_clean = df_series[relevant_cols].copy()

# Handle missing data definitions safely
df_clean["topic"] = df_clean["topic"].cat.add_categories("Unknown").fillna("Unknown")

# Export clean metadata
df_clean.to_csv("../data/IDS_SeriesMetaData_cleaned.csv", index=False)
print("\n[Success] Standardized data exported to 'IDS_SeriesMetaData_cleaned.csv'")

# =====================================================================
# 3. EXPLORATORY DATA ANALYSIS (EDA)
# =====================================================================
print("\n=== 3. EXPLORATORY DATA ANALYSIS ===")

# A. Statistical Summaries of Core Macro Components
print("\n--- Distribution of Indicators by Debt Topic ---")
topic_counts = df_clean["topic"].value_counts()
print(topic_counts)

print("\n--- Distribution of Aggregation Methods Used ---")
print(df_clean["aggregation_method"].value_counts())

# B. Identification of Top Debt Indicators & Impact Areas
print("\n--- Top 3 Heavily Represented Macro Debt Categories ---")
for topic, count in topic_counts.head(3).items():
    print(f" * {topic.replace('Economic Policy & Debt: External debt: ', '')}: {count} specific metrics tracked")

# C. Trend Visualization: Structural Breakdown Chart
plt.figure(figsize=(12, 6))
sns.countplot(
    data=df_clean,
    y="topic",
    hue="topic",
    order=df_clean["topic"].value_counts().index,
    palette="viridis",
    legend=False
)
plt.title("Volume of Specific Debt Metrics Monitored by Strategic Sub-Topic")
plt.xlabel("Count of Registered Structural Indicators")
plt.ylabel("Macro Economic / Debt Topic Category")
plt.tight_layout()
plt.savefig("debt_indicator_topic_distribution.png")
print("\n📈 Structural EDA Barplot successfully saved as 'debt_indicator_topic_distribution.png'")
plt.show()