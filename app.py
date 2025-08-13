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