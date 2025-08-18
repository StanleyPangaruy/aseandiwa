import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import base64
from io import BytesIO
import json

# Page configuration
st.set_page_config(
    page_title="ASEAN-DIWA Dashboard",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Sidebar navigation
st.sidebar.title("🌏 ASEAN-DIWA")
st.sidebar.markdown("Digital Innovation for Women Advancement in ASEAN")

st.sidebar.markdown("---")

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Dashboard"

# Navigation buttons
st.sidebar.subheader("📋 Navigation")

if st.sidebar.button("🏠 Dashboard", use_container_width=True):
    st.session_state.current_page = "Dashboard"
    
if st.sidebar.button("🗺️ ASEAN Map", use_container_width=True):
    st.session_state.current_page = "ASEAN Map"
    
if st.sidebar.button("📊 Country Profiles", use_container_width=True):
    st.session_state.current_page = "Country Profiles"
    
if st.sidebar.button("📈 Comparison", use_container_width=True):
    st.session_state.current_page = "Comparison"
    
if st.sidebar.button("ℹ️ About", use_container_width=True):
    st.session_state.current_page = "About"

page = st.session_state.current_page

# Dashboard Page
if page == "Dashboard":
    st.markdown("""
    <div class="main-header">
        <h1>ASEAN Digital Innovation for Women Advancement (DIWA)</h1>
        <p>Bridging the Digital Gender Gap in Southeast Asia</p>
    </div>
    """, unsafe_allow_html=True)
    

# ASEAN Map Page
elif page == "ASEAN Map":
    st.title("🗺️ ASEAN Interactive Map")
    st.markdown("Explore digital innovation indicators across ASEAN countries")
    

# Country Profiles Page
elif page == "Country Profiles":
    st.title("📊 Country Profiles")
    st.markdown("Detailed analysis for each ASEAN country")
    
    # Country selection
    countries = sorted(df['Country'].unique())
    
    # Create country grid
    cols = st.columns(4)
    selected_country = None
    
    for i, country in enumerate(countries):
        with cols[i % 4]:
            if st.button(f"🏴 {country}", key=f"country_{i}", use_container_width=True):
                selected_country = country
    
    # Use session state to persist selection
    if 'selected_country' not in st.session_state:
        st.session_state.selected_country = countries[0]
    
    if selected_country:
        st.session_state.selected_country = selected_country
    
    country = st.session_state.selected_country
    
    st.markdown(f"## 📍 {country} Profile")
    
    # Country overview
    country_data = df[df['Country'] == country]
    
    # Latest year data
    latest_year = country_data['Year'].max()
    latest_data = country_data[country_data['Year'] == latest_year]
    
    # Overview metrics
    st.subheader("📊 Key Indicators Overview")
    
    cols = st.columns(3)
    for j, (_, row) in enumerate(latest_data.iterrows()):
        with cols[j % 3]:
            st.metric(row['Indicator'], f"{row['Value']:.1f}")
    
    # Trends analysis
    st.subheader("📈 Trends Over Time")
    
    trend_indicator = st.selectbox("Select Indicator for Trends:", 
                                  country_data['Indicator'].unique(),
                                  key="trend_indicator")
    
    trend_data = country_data[country_data['Indicator'] == trend_indicator]
    
    fig = px.line(trend_data, x='Year', y='Value',
                 title=f'{trend_indicator} Trends in {country}',
                 markers=True)
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Country summary
    st.subheader("📝 Country Summary")
    
    avg_all = latest_data['Value'].mean()
    strongest_indicator = latest_data.nlargest(1, 'Value')['Indicator'].iloc[0]
    weakest_indicator = latest_data.nsmallest(1, 'Value')['Indicator'].iloc[0]
    
    summary_text = f"""
    **{country}** shows an average digital inclusion score of **{avg_all:.1f}** across all indicators in {latest_year}.
    
    **Key Insights:**
    - Strongest Indicator: {strongest_indicator}
    - Area for Improvement: {weakest_indicator}
    
    **Recommendations:**
    - Continue strengthening digital infrastructure and affordability
    - Promote inclusive digital policies and programs
    - Monitor progress across all key indicators
    """
    
    st.markdown(summary_text)
    
    # Download section
    st.subheader("📥 Download Report")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📄 Download PDF Report"):
            st.info("PDF download functionality would be implemented with additional libraries")
    
    with col2:
        if st.button("🖼️ Download PNG Chart"):
            st.info("PNG download functionality would be implemented with additional libraries")
    
    # Raw data download
    country_csv = country_data.to_csv(index=False)
    st.download_button(
        label="📊 Download Raw Data (CSV)",
        data=country_csv,
        file_name=f'{country}_digital_inclusion_data.csv',
        mime='text/csv'
    )
    

# Comparison Page
elif page == "Comparison":
    st.title("📈 Country Comparison")
    st.markdown("Compare digital innovation indicators across countries")
    

# About Page
elif page == "About":
    st.title("ℹ️ About ASEAN-DIWA")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "© 2024 ASEAN-DIWA | Digital Innovation for Women Advancement in ASEAN | "
    "Dashboard v1.0"
    "</div>", 
    unsafe_allow_html=True
)