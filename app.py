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
    st.markdown("Explore digital inclusion indicators across ASEAN countries")
    
    # Map controls
    map_indicator = st.selectbox("Select Indicator for Map:", df['Indicator'].unique())
    
    # Prepare map data — pick the latest year for each country
    map_data = df[df['Indicator'] == map_indicator].copy()
    map_data = map_data.loc[map_data.groupby('Country')['Year'].idxmax()]
    
    # Add coordinates
    map_data['lat'] = map_data['Country'].map(lambda x: country_coords.get(x, {}).get('lat', None))
    map_data['lon'] = map_data['Country'].map(lambda x: country_coords.get(x, {}).get('lon', None))

    
    
    # Create choropleth-style scatter map
    fig = px.choropleth(
        map_data,
        locations="Country",               # Country names in your dataset
        locationmode="country names",      # Plotly will map them automatically
        color="Value",                     # Replace with your metric column
        hover_name="Country",              # Show country name on hover
        color_continuous_scale="Viridis",  # Color scale
        projection="natural earth"         # World map projection
    )
    
    fig.update_layout(
        geo=dict(
            showcountries=True,
            showcoastlines=True,
            showland=True,
            fitbounds="locations"
        ),
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Country comparison section
    st.subheader("🔄 Quick Country Comparison")
    
    col1, col2 = st.columns(2)
    with col1:
        country1 = st.selectbox("Select First Country:", map_data['Country'].unique())
    with col2:
        country2 = st.selectbox("Select Second Country:", 
                               [c for c in map_data['Country'].unique() if c != country1])
    
    if country1 and country2:
        comp_data = map_data[map_data['Country'].isin([country1, country2])]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            val1 = comp_data[comp_data['Country'] == country1]['Value'].iloc[0]
            st.metric(country1, f"{val1:.1f}")
        
        with col2:
            val2 = comp_data[comp_data['Country'] == country2]['Value'].iloc[0]
            diff = val2 - val1
            st.metric(country2, f"{val2:.1f}", f"{diff:+.1f}")
        
        with col3:
            st.markdown(f"**Gap:** {abs(diff):.1f} percentage points")
    

# Country Profiles Page
elif page == "Country Profiles":
    st.title("📊 Country Profiles")
    st.markdown("Detailed analysis for each ASEAN country")
    

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