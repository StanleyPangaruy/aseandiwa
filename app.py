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


    

elif page == "Data Stories":
    st.title("📖 Data Stories")
    st.markdown("Insights and analysis through data-driven narratives")
    
    # Story 1
    st.markdown("""
    <div class="story-card">
        <div class="story-meta">📅 Published: March 15, 2024 | 👤 By: ASEAN-DIWA Research Team</div>
        <div class="story-title">Bridging the Digital Divide: Women's Internet Access in ASEAN</div>
        <div class="story-excerpt">
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure 
    dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    
    **Sed ut perspiciatis unde omnis** iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, 
    eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam 
    voluptatem quia voluptas sit aspernatur aut odit aut fugit.
    """)
    
    # Image placeholder for Story 1
    st.markdown("""
    <div style="background-color: #f8f9fa; border: 2px dashed #e91e63; padding: 2rem; text-align: center; border-radius: 10px; margin: 1rem 0;">
        <h4 style="color: #e91e63;">📊 Chart: Internet Usage Gender Gap Across ASEAN Countries</h4>
        <p style="color: #666;">Image placeholder - Add your data visualization asset here</p>
        <p style="font-size: 0.9rem; color: #999;">Recommended size: 800x400px | Format: PNG/JPG</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti 
    quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia 
    deserunt mollitia animi, id est laborum et dolorum fuga.
    
    **Et harum quidem rerum** facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio 
    cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.
    """)
    
    st.markdown("---")
    
    # Story 2
    st.markdown("""
    <div class="story-card">
        <div class="story-meta">📅 Published: February 28, 2024 | 👤 By: Gender Digital Inclusion Team</div>
        <div class="story-title">Mobile Revolution: How Smartphones are Empowering Women Entrepreneurs</div>
        <div class="story-excerpt">
        "Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae."
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae 
    sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus 
    maiores alias consequatur aut perferendis doloribus asperiores repellat.
    
    **Consectetur adipiscing elit**, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    """)
    
    # Image placeholder for Story 2
    st.markdown("""
    <div style="background-color: #f8f9fa; border: 2px dashed #e91e63; padding: 2rem; text-align: center; border-radius: 10px; margin: 1rem 0;">
        <h4 style="color: #e91e63;">📈 Chart: Mobile Phone Ownership Progress Over Time</h4>
        <p style="color: #666;">Image placeholder - Add your data visualization asset here</p>
        <p style="font-size: 0.9rem; color: #999;">Recommended size: 800x400px | Format: PNG/JPG</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. 
    Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium.
    
    **Totam rem aperiam**, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. 
    Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit.
    """)
    
    st.markdown("---")
    
    # Story 3
    st.markdown("""
    <div class="story-card">
        <div class="story-meta">📅 Published: January 20, 2024 | 👤 By: Digital Skills Research Unit</div>
        <div class="story-title">The Skills Gap: Digital Literacy Challenges for Women in Southeast Asia</div>
        <div class="story-excerpt">
        "Sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem."
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    Sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. 
    Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea 
    commodi consequatur.
    
    **Quis autem vel eum** iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum 
    qui dolorem eum fugiat quo voluptas nulla pariatur. At vero eos et accusamus et iusto odio dignissimos ducimus qui 
    blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias.
    """)
    
    # Image placeholder for Story 3
    st.markdown("""
    <div style="background-color: #f8f9fa; border: 2px dashed #e91e63; padding: 2rem; text-align: center; border-radius: 10px; margin: 1rem 0;">
        <h4 style="color: #e91e63;">📊 Chart: Women's Digital Literacy by Country</h4>
        <p style="color: #666;">Image placeholder - Add your data visualization asset here</p>
        <p style="font-size: 0.9rem; color: #999;">Recommended size: 800x500px | Format: PNG/JPG</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    Excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, 
    id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio.
    
    **Nam libero tempore**, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat 
    facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.
    """)
    
    st.markdown("---")
    
    # Story 4
    st.markdown("""
    <div class="story-card">
        <div class="story-meta">📅 Published: December 10, 2023 | 👤 By: Economic Empowerment Team</div>
        <div class="story-title">From Code to Career: Women Breaking Barriers in ICT Employment</div>
        <div class="story-excerpt">
        "Ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat."
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        Ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        
        **Duis aute irure dolor** in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        
        Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, 
        eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.
        """)
    
    with col2:
        # Mini statistics placeholder
        st.markdown("""
        <div style="background-color: #fce4ec; border: 2px dashed #e91e63; padding: 1rem; text-align: center; border-radius: 10px;">
            <h4 style="color: #e91e63;">📊 ICT Employment Stats</h4>
            <p style="color: #666;">Statistics card placeholder</p>
            <p style="font-size: 0.8rem; color: #999;">Add your stats here</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Story 4 main chart placeholder
    st.markdown("""
    <div style="background-color: #f8f9fa; border: 2px dashed #e91e63; padding: 2rem; text-align: center; border-radius: 10px; margin: 1rem 0;">
        <h4 style="color: #e91e63;">📈 Chart: ICT Employment Trends by Gender</h4>
        <p style="color: #666;">Image placeholder - Add your data visualization asset here</p>
        <p style="font-size: 0.9rem; color: #999;">Recommended size: 800x400px | Format: PNG/JPG</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Related Stories Section
    st.subheader("🔗 Related Stories")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **📱 Digital Banking Adoption**  
        *Coming Soon*
        
        Exploring how women in rural ASEAN communities are embracing digital financial services...
        """)
    
    with col2:
        st.markdown("""
        **🛒 E-commerce Trends**  
        *Coming Soon*
        
        The rise of women-led online businesses and the impact on economic empowerment...
        """)
    
    with col3:
        st.markdown("""
        **🎓 Digital Education Access**  
        *Coming Soon*
        
        How online learning platforms are creating new opportunities for women...
        """)
    
    # Newsletter signup
    st.markdown("---")
    st.subheader("📧 Stay Updated")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.text_input("Enter your email for updates on new data stories", placeholder="your.email@example.com")
    with col2:
        if st.button("Subscribe", use_container_width=True):
            st.success("Thank you for subscribing!")

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