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
    

# Comparison Page
elif page == "Comparison":
    st.title("📈 Country Comparison")
    st.markdown("Compare digital inclusion indicators across countries (all years)")

    # Comparison controls
    col1, col2, col3 = st.columns(3)

    with col1:
        comp_indicator = st.selectbox("Select Indicator:", df['Indicator'].unique())

    with col2:
        comp_countries = st.multiselect(
            "Select Countries to Compare:",
            df['Country'].unique(),
            default=df['Country'].unique()[:5]
        )
    with col3:
        chart_type = st.selectbox("Chart Type:", ["Bar Chart", "Line Chart"])

    if comp_countries:
        # Filter data for indicator + countries (no year filter)
        comp_data = df[
            (df['Indicator'] == comp_indicator) &
            (df['Country'].isin(comp_countries))
        ]

        # Create visualizations
        if chart_type == "Bar Chart":
            # Show the most recent year's values for each country
            latest_years = comp_data.groupby("Country")["Year"].max().reset_index()
            comp_latest = comp_data.merge(latest_years, on=["Country", "Year"])

            fig = px.bar(
                comp_latest,
                x='Country',
                y='Value',
                color='Country',
                title=f'{comp_indicator} (Most Recent Year)',
            )
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)

        elif chart_type == "Line Chart":
            # Show trends over time
            fig = px.line(
                comp_data,
                x='Year',
                y='Value',
                color='Country',
                title=f'{comp_indicator} Trends Over Time',
                markers=True,
                color_discrete_sequence=px.colors.qualitative.Set1
            )
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)

        # Rankings based on most recent year
        latest_years = comp_data.groupby("Country")["Year"].max().reset_index()
        comp_latest = comp_data.merge(latest_years, on=["Country", "Year"])
        comp_latest = comp_latest.sort_values('Value', ascending=False).reset_index(drop=True)
        comp_latest['Rank'] = comp_latest.index + 1

        st.subheader("🏆 Rankings")
        st.dataframe(
            comp_latest[['Rank', 'Country', 'Value']].rename(columns={'Value': f'{comp_indicator}'}),
            use_container_width=True
        )

        # Download options
        st.subheader("📥 Download Options")
        col1, col2 = st.columns(2)
        with col1:
            csv = comp_data.to_csv(index=False)
            st.download_button(
                label="📊 Download Full Data (CSV)",
                data=csv,
                file_name=f'comparison_{comp_indicator}_all_years.csv',
                mime='text/csv'
            )

        with col2:
            st.info("📈 Chart download functionality would be implemented with additional libraries")
    

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