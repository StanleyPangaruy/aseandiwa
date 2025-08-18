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

# Custom CSS with women-focused color scheme
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #e91e63 0%, #ad1457 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 8px rgba(233, 30, 99, 0.3);
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(233, 30, 99, 0.1);
        text-align: center;
        border-top: 3px solid #e91e63;
    }
    .country-card {
        background: #fce4ec;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #e91e63;
        margin-bottom: 1rem;
    }
    .indicator-section {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(233, 30, 99, 0.05);
        border-left: 4px solid #f8bbd9;
    }
    
    .story-card {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 8px rgba(233, 30, 99, 0.1);
        border-top: 4px solid #e91e63;
    }
    
    .story-meta {
        color: #ad1457;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    
    .story-title {
        color: #e91e63;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .story-excerpt {
        color: #666;
        font-style: italic;
        margin-bottom: 1rem;
        padding-left: 1rem;
        border-left: 3px solid #f8bbd9;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #fce4ec;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #e91e63, #ad1457);
        color: white;
        border: none;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #ad1457, #880e4f);
        box-shadow: 0 4px 8px rgba(233, 30, 99, 0.3);
        transform: translateY(-2px);
    }
    
    /* Selectbox and other input styling */
    .stSelectbox > div > div {
        border-color: #e91e63;
    }
    
    /* Metric value styling */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #fce4ec, #f8bbd9);
        border: 1px solid #e91e63;
        padding: 1rem;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Generate sample data

@st.cache_data
def load_diwa_data():
    # Load CSV
    df = pd.read_csv("data/diwa.csv")
    
    # Ensure column names match expected format
    df.columns = df.columns.str.strip()  # remove extra spaces
    
    # Rename columns for consistency with Streamlit app logic
    df = df.rename(columns={
        "country": "Country",
        "year": "Year",
        "indicator_name": "Indicator",
        "indicator_value": "Value",
        "subnational": "Subnational",
        "remarks": "Remarks",
        "source": "Source",
        "source_url": "SourceURL"
    })
    
    # Clean up data types
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
    
    # Drop rows without a valid year or value
    df = df.dropna(subset=["Year", "Value"])
    
    # Optional: sort for cleaner display
    df = df.sort_values(by=["Country", "Year", "Indicator"])
    
    return df



# Country coordinates for map
@st.cache_data
def get_country_coordinates():
    return {
        'Brunei': {'lat': 4.5353, 'lon': 114.7277},
        'Cambodia': {'lat': 12.5657, 'lon': 104.9910},
        'Indonesia': {'lat': -0.7893, 'lon': 113.9213},
        'Laos': {'lat': 19.8563, 'lon': 102.4955},
        'Malaysia': {'lat': 4.2105, 'lon': 101.9758},
        'Myanmar': {'lat': 21.9162, 'lon': 95.9560},
        'Philippines': {'lat': 12.8797, 'lon': 121.7740},
        'Singapore': {'lat': 1.3521, 'lon': 103.8198},
        'Thailand': {'lat': 15.8700, 'lon': 100.9925},
        'Vietnam': {'lat': 14.0583, 'lon': 108.2772},
        'Papua New Guinea': {'lat': -6.3150, 'lon': 143.9555},
        'Timor-Leste': {'lat': -8.8742, 'lon': 125.7275}
    }

# Initialize data
df = load_diwa_data()
country_coords = get_country_coordinates()

# Sidebar navigation
st.sidebar.title("🌏 ASEAN-DIWA")
st.sidebar.markdown("Digital Inclusion for Women in ASEAN")

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

if st.sidebar.button("📈 Data Stories", use_container_width=True):
    st.session_state.current_page = "Data Stories"
    
if st.sidebar.button("ℹ️ About", use_container_width=True):
    st.session_state.current_page = "About"

page = st.session_state.current_page

# Dashboard Page
if page == "Dashboard":
    st.markdown("""
    <div class="main-header">
        <h1>ASEAN Digital Inclusion for Women Alliance (DIWA)</h1>
        <p>Bridging the Digital Gender Gap in Southeast Asia</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project Brief
    with st.expander("📋 Project Brief", expanded=True):
        st.markdown("""
        **ASEAN-DIWA** is a comprehensive initiative aimed at promoting digital inclusion and reducing 
        the digital gender gap across ASEAN member states and partner countries. Our mission is to:
        
        - 📊 **Monitor** digital gender disparities through data-driven insights  
        - 🎯 **Identify** key areas requiring targeted interventions  
        - 🤝 **Collaborate** with stakeholders to implement inclusive digital policies  
        - 📈 **Track** progress towards achieving digital equality
        
        This dashboard provides interactive visualizations and country-specific analysis to support 
        evidence-based decision making for digital inclusion initiatives.
        """)
    
    # Key Metrics Overview
    st.subheader("📊 Key Indicators Overview")
    
    # Filter controls
    selected_countries = st.multiselect(
        "Select Countries:",
        options=df['Country'].unique(),
        default=df['Country'].unique()[:6]
    )
    
    # Filter data
    filtered_data = df[df['Country'].isin(selected_countries)]
    
    # Compute average per indicator and pick top 8
    indicator_means = (
        filtered_data.groupby("Indicator")["Value"]
        .mean()
        .sort_values(ascending=False)
        .head(8)
    )

    # Create metrics cards (limit to 8 indicators)
    indicators = filtered_data['Indicator'].unique()[:8]
    
    # Create metrics cards
    # indicators = filtered_data['Indicator'].unique()
    cols = st.columns(4)
    for i, indicator in enumerate(indicators):
        with cols[i % 4]:
            indicator_data = filtered_data[filtered_data['Indicator'] == indicator]
            avg_value = indicator_data['Value'].mean()
            
            if pd.notna(avg_value):
                st.markdown(f"""
                <div class="metric-card">
                    <h3>{indicator}</h3>
                    <h2 style="color: #e91e63;">{avg_value:.1f}</h2>
                    <p>Average across selected countries (all years)</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Navigation Guide
    st.subheader("🧭 Explore More")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="indicator-section">
            <h4>🗺️ Interactive Map</h4>
            <p>Explore geographical patterns of digital inclusion across ASEAN countries with our interactive choropleth maps.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Visit ASEAN Map", key="map_btn"):
            st.session_state.current_page = "ASEAN Map"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="indicator-section">
            <h4>📊 Country Profiles</h4>
            <p>Dive deep into individual country analysis with detailed breakdowns and downloadable reports.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("View Country Profiles", key="profile_btn"):
            st.session_state.current_page = "Country Profiles"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="indicator-section">
            <h4>📈 Compare Countries</h4>
            <p>Create side-by-side comparisons between countries with customizable charts and rankings.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Compare Countries", key="compare_btn"):
            st.session_state.current_page = "Comparison"
            st.rerun()
    

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