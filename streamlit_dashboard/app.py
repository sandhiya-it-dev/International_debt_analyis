import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from database import get_engine

# =========================================================================
# 1. PAGE SETUP & STYLING
# =========================================================================
# st.set_page_config must be the first Streamlit command executed in the script.
# It configures the browser tab title and stretches the layout to use the full screen width.
st.set_page_config(page_title="International Debt Analytics", layout="wide")

# Render primary text headers and an aesthetic markdown horizontal divider line.
st.title("🌍 International Debt Statistics | Advanced Visual Dashboard")
st.markdown("---")

# =========================================================================
# 2. DATABASE ENGINE CONNECTION
# =========================================================================
# @st.cache_resource keeps the database engine alive across app refreshes/reruns.
# Instead of establishing a slow, new connection pool on every user click, it reuses the existing one.
@st.cache_resource
def init_db_engine():
    return get_engine()

# Initialize an empty state tracking variable for the connection engine.
engine = None

try:
    # Trigger the cached connection pool generator function.
    engine = init_db_engine()
    
    # Run a rapid, lightweight connection test. If the database credentials or server 
    # are down, this context manager block throws an immediate catchable exception.
    with engine.connect() as conn:
        pass 
except Exception as e:
    # Safely halt application UI deployment if infrastructure links are broken.
    st.error(f"❌ Connection Failed: {e}")
    st.stop()

# =========================================================================
# 3. SIDEBAR FILTERS
# =========================================================================
# Instantiate an isolated controller panel along the left edge of the screen viewport.
st.sidebar.header("Global Filters")

try:
    # Run a quick query to extract only the unique geographic regions present in the dataset.
    regions_df = pd.read_sql(
        "SELECT DISTINCT region FROM public.countries WHERE region IS NOT NULL AND region <> '';", 
        engine
    )
    
    # Construct a clean Python selection list. We append a default 'All Regions' option 
    # to the front of our sorted database categories so users can look at everything globally.
    regions_list = ["All Regions"] + list(regions_df["region"].sort_values())
    
    # Render the selection dropdown widget. Streamlit assigns the chosen string to 'selected_region'.
    selected_region = st.sidebar.selectbox("Geographic Region", regions_list)
except Exception as e:
    # Fallback exception boundary ensuring a minor query glitch won't break the global UI state.
    st.sidebar.error(f"Error loading filters: {e}")
    selected_region = "All Regions"

# =========================================================================
# 4. DATA EXTRACTION LAYER
# =========================================================================
# Query 1: Country Rankings Aggregation
# Combines the debt record table with country metadata via an inner join. Groups data 
# by individual country names to compute their absolute sum of accumulated debt.
query_country_rankings = """
    SELECT c.long_name AS country_name, c.region, c.income_group, SUM(d.debt_value) AS total_debt_usd
    FROM public.debt_data d
    JOIN public.countries c ON d.country_code = c.country_code
    WHERE c.region IS NOT NULL AND c.region <> '' AND d.debt_value > 0
    GROUP BY c.long_name, c.region, c.income_group;
"""

# Query 2: Structural Financial Indicators Aggregation
# Joins tables to aggregate debt values explicitly under indicator codes/names (e.g., Short-term debt).
# Keeps regional categories intact so it can be dynamically sliced later by our sidebar filter.
query_indicators = """
    SELECT d.indicator_name, c.region, SUM(d.debt_value) AS total_debt_usd
    FROM public.debt_data d
    JOIN public.countries c ON d.country_code = c.country_code
    WHERE d.debt_value > 0 AND c.region IS NOT NULL AND c.region <> ''
    GROUP BY d.indicator_name, c.region
    ORDER BY total_debt_usd DESC;
"""

# Query 3: Time Series Macro Trend Tracking
# Aggregates raw global debt balances chronologically by fiscal calendar years. 
# Categorizes pools dynamically across socioeconomic wealth structures (income groups).
query_trends = """
    SELECT d.year, c.income_group, SUM(d.debt_value) AS annual_debt_usd
    FROM public.debt_data d
    JOIN public.countries c ON d.country_code = c.country_code
    WHERE c.income_group IS NOT NULL AND c.income_group <> ''
    GROUP BY d.year, c.income_group
    ORDER BY d.year ASC;
"""

try:
    # Pull data frames into memory using pandas execution blocks reading off the SQLAlchemy engine.
    df_countries = pd.read_sql(query_country_rankings, engine)
    df_indicators = pd.read_sql(query_indicators, engine)
    df_trends = pd.read_sql(query_trends, engine)
except Exception as e:
    # Safely halt execution if a database table column mapping fails to parse.
    st.error(f"Error processing relational metrics: {e}")
    st.stop()

# Evaluate dynamic interactive slice transformations based on sidebar dropdown selections.
if selected_region != "All Regions":
    # If a specific region is picked, filter out row records that do not belong to that subset.
    df_countries = df_countries[df_countries["region"] == selected_region]
    df_indicators = df_indicators[df_indicators["region"] == selected_region]

# Slice raw data structures into explicit top-10 segments to prevent visual graph clutter.
# df_highest grabs the 10 largest debt values; df_lowest grabs the 10 smallest debt values.
df_highest = df_countries.sort_values(by="total_debt_usd", ascending=False).head(10)
df_lowest = df_countries.sort_values(by="total_debt_usd", ascending=True).head(10)

# Re-aggregate the filtered indicator data by structural category names to prepare it for Seaborn mapping.
df_top_indicators = df_indicators.groupby("indicator_name")["total_debt_usd"].sum().reset_index().sort_values(by="total_debt_usd", ascending=False).head(10)

# =========================================================================
# 5. INDUSTRIAL COMPONENT LAYOUT TABS
# =========================================================================
# Split the web dashboard interface cleanly into distinct tab pages.
tab1, tab2, tab3 = st.tabs(["📊 Country-Wise Distributions", "🧩 Indicator Breakdowns", "📈 Microscopic Trend Patterns"])

# -------------------------------------------------------------------------
# TAB 1: Country-Wise Analysis (Plotly Express Interactive Engine)
# -------------------------------------------------------------------------
with tab1:
    st.subheader("Geographic and Institutional Concentration Profiles")
    # Form a split layout creating two horizontal columns with an identical size ratio.
    col1, col2 = st.columns(2)
    
    with col1:
        # Render the horizontal bar chart showing the highest debt profiles.
        if not df_highest.empty:
            fig_high = px.bar(
                df_highest, x="total_debt_usd", y="country_name", orientation='h',
                color="income_group", title=f"Top 10 Highest Debt Profiles ({selected_region})",
                template="plotly_dark", color_discrete_sequence=px.colors.qualitative.Pastel
            )
            # categoryorder='total ascending' sorts the horizontal chart bars so the largest bar stays at the top.
            fig_high.update_layout(yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig_high, use_container_width=True)
        else:
            st.info("No distribution records match the selection criteria.")

    with col2:
        # Render the horizontal bar chart showing the lowest debt profiles.
        if not df_lowest.empty:
            fig_low = px.bar(
                df_lowest, x="total_debt_usd", y="country_name", orientation='h',
                color="income_group", title=f"Top 10 Lowest Debt Profiles ({selected_region})",
                template="plotly_dark", color_discrete_sequence=px.colors.qualitative.Pastel
            )
            # categoryorder='total descending' ensures the lowest borrowing countries display clearly in order.
            fig_low.update_layout(yaxis={'categoryorder':'total descending'})
            st.plotly_chart(fig_low, use_container_width=True)

# -------------------------------------------------------------------------
# TAB 2: Indicator Analysis (Matplotlib & Seaborn Component Framework)
# -------------------------------------------------------------------------
with tab2:
    st.subheader("Structural Debt Distribution Across Economic Metrics")
    
    if not df_top_indicators.empty:
        # 1. Instantiate coordinate axes and a static drawing canvas space via Matplotlib.
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # 2. Match graph background color spaces to the main web app dashboard aesthetic theme.
        plt.style.use("dark_background")
        ax.set_facecolor("#111111")
        fig.patch.set_facecolor("#111111")
        
        # 3. Direct Seaborn to paint an organized horizontal barplot onto the Matplotlib axes frame.
        # hue="indicator_name" combined with legend=False explicitly applies unique category styling.
        sns.barplot(
            data=df_top_indicators,
            x="total_debt_usd",
            y="indicator_name",
            ax=ax,
            palette="viridis",
            hue="indicator_name",
            legend=False
        )
        
        # 4. Apply clean descriptive layout properties over visual typography labels and ticks.
        ax.set_title("Top 10 Heavy Structural Drivers of External Debt", fontsize=14, pad=15, color="white")
        ax.set_xlabel("Accumulated Debt Asset Pool (USD)", fontsize=11, color="white")
        ax.set_ylabel("", fontsize=11)
        ax.tick_params(colors="white", labelsize=9)
        plt.tight_layout()
        
        # 5. Pass the final custom Matplotlib figure variable into the native Streamlit drawing engine.
        st.pyplot(fig)
    else:
        st.info("Insufficient indicator volumes found to render distribution vectors.")

# -------------------------------------------------------------------------
# TAB 3: Trends Over Time (Plotly Express Line Tracking Engine)
# -------------------------------------------------------------------------
with tab3:
    st.subheader("Macro-Fiscal Trajectories Over Time")
    
    # Track historical debt changes using an interactive continuous timeline chart.
    if not df_trends.empty:
        fig_line = px.line(
            df_trends, x="year", y="annual_debt_usd", color="income_group", markers=True,
            labels={"annual_debt_usd": "Aggregate Debt Vault (USD)", "year": "Fiscal Tracking Cycle"},
            title="Long-Term Financial Leverage Progression by Economic Stratum",
            template="plotly_dark", color_discrete_sequence=px.colors.qualitative.Safe
        )
        # Scale chart width fluidly to fill out the browser layout context.
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.info("Time-series tracking elements are currently empty.")