import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure relative paths work flawlessly
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

# 1. Load the dataset
df = pd.read_csv("../data/Country-Series - Metadata.csv", encoding="cp1252")

# Standardize column names into clean snake_case
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_", regex=False)
      .str.replace("-", "_", regex=False)
)

print("Missing values per column:\n", df.isna().sum())

# Remove duplicates up front
df = df.drop_duplicates()

# 2. Safely Convert Column Data Types
for col in ["country_code", "series_code", "description"]:
    if col in df.columns:
        df[col] = df[col].astype("string")

# Convert 'type' ONLY if it exists in your dataset's columns
if "type" in df.columns:
    df["type"] = df["type"].astype("category")

# 3. Vectorized Extractions (Fast & handles hyphens like ABC-123)
if "country_code" in df.columns:
    # Extracts everything before the parentheses as country_name, and the 3 letters inside as short_code
    country_parts = df["country_code"].str.extract(r"^(.*?)\s*\(([A-Z]{3})\)$")
    df["country_name"] = country_parts[0].str.strip()
    df["country_short_code"] = country_parts[1].fillna("Unknown")

if "series_code" in df.columns:
    # Captures the alphanumeric code inside the final parentheses, supporting dots and hyphens
    df["indicator_code"] = df["series_code"].str.extract(r"\(([A-Z0-9\.\-]+)\)$").fillna("Unknown")
    # Captures everything before that final set of parentheses
    df["indicator_name"] = df["series_code"].str.replace(r"\s*\([A-Z0-9\.\-]+\)$", "", regex=True).str.strip()

# 4. Filter, Reorder, and Export
available_cols = [
    col for col in [
        "type", "country_code", "country_name", "country_short_code",
        "series_code", "indicator_name", "indicator_code", "description"
    ] if col in df.columns
]

meta = df[available_cols].copy()
meta.to_csv("../data/country_series_metadata_cleaned.csv", index=False)
print("\n=============================================")
print(" Cleaned metadata saved successfully!")
print(f"Final shape: {meta.shape}")
print("=============================================")

# =====================================================================
# 5. METADATA EXPLORATORY DATA ANALYSIS (EDA)
# =====================================================================
print("\n=============================================")
print("     METADATA EXPLORATORY DATA ANALYSIS      ")
print("=============================================\n")

# 1. Distribution of Metadata Types
if "type" in meta.columns and meta["type"].notnull().sum() > 0:
    print("--- Distribution by Metadata Type ---")
    print(meta["type"].value_counts())
    print("-" * 40)

# 2. Top Countries with the Most Metadata Links
print("--- Top 10 Countries with Most Metadata Records ---")
country_counts = meta["country_name"].value_counts()
print(country_counts.head(10))
print("-" * 40)

# 3. Top Indicators requiring specialized Metadata definitions
print("--- Top 10 Indicators with Most Metadata Records ---")
indicator_counts = meta["indicator_name"].value_counts()
print(indicator_counts.head(10))
print("-" * 40)

# 4. Generate an EDA Visualization Plot
plt.figure(figsize=(14, 6))

# Subplot 1: Top Countries
plt.subplot(1, 2, 1)
sns.barplot(
    x=country_counts.head(10).values,
    y=country_counts.head(10).index,
    hue=country_counts.head(10).index,
    palette="Purples_r",
    legend=False
)
plt.title("Top 10 Countries by Metadata Volume")
plt.xlabel("Number of Metadata Rows")

# Subplot 2: Top Indicators
plt.subplot(1, 2, 2)
sns.barplot(
    x=indicator_counts.head(10).values,
    y=[name[:40] + "..." if len(name) > 40 else name for name in indicator_counts.head(10).index],
    hue=indicator_counts.head(10).index,
    palette="Oranges_r",
    legend=False
)
plt.title("Top 10 Indicators by Metadata Volume")
plt.xlabel("Number of Metadata Rows")

plt.tight_layout()
plt.savefig("country_series_metadata_eda.png")
print("\n📈 EDA Visualization saved successfully as 'country_series_metadata_eda.png'!")
plt.show()