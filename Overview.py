import os
import streamlit as st

st.set_page_config(page_title='EDEN CARE DASHBOARDS', page_icon="EC_logo.png", layout="wide")

st.sidebar.success("Select a page above.")

def main():
    # Custom CSS to style the dashboard
    st.markdown("""
        <style>
            .main-title {
                color: #e66c37; /* Title color */
                text-align: center; /* Center align the title */
                font-size: 3rem; /* Title font size */
                font-weight: bold; /* Title font weight */
                margin-bottom: .5rem; /* Space below the title */
                text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1); /* Subtle text shadow */
            }
            div.block-container {
                padding-top: 2rem; /* Padding for main content */
            }

            .subheader {
                color: #e66c37;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
                padding: 10px;
                border-radius: 5px;
                display: inline-block;
            }
            .section-title {
                font-size: 1.75rem;
                color: #004d99;
                margin-top: 2rem;
                margin-bottom: 0.5rem;
            }
            .text {
                font-size: 1.1rem;
                color: #333;
                padding: 10px;
                line-height: 1.6;
                margin-bottom: 1rem;
            }
            .nav-item {
                font-size: 1.2rem;
                color: #004d99;
                margin-bottom: 0.5rem;
            }
            .separator {
                margin: 2rem 0;
                border-bottom: 2px solid #ddd;
            }
                
        </style>
    """, unsafe_allow_html=True)

    # Title and Subheader
    st.markdown('<h1 class="main-title">EDEN CARE MEDICAL DASHBOARD</h1>', unsafe_allow_html=True)

    st.image("undraw_analytics_re_dkf8.svg", caption='Eden Care Medical', use_column_width=True)

    st.markdown('<h2 class="subheader">Welcome to the Eden Care Medical Dashboard</h2>', unsafe_allow_html=True)

    # Introduction
    st.markdown('<div class="text">These dashboards are designed to provide insights into the three key processes of our insurance operations: Visits, Claims, and Preauthorization. Each section of the dashboard is dedicated to one of these processes, offering detailed visualizations and analyses to help improve operational efficiency and enhance the customer experience.</div>', unsafe_allow_html=True)

    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    # Processes Overview
    col1, col2 = st.columns((2))
    with col1:
        st.markdown('<h2 class="subheader">VISIT MANAGEMENT</h2>', unsafe_allow_html=True)
        st.markdown('<div class="text"><strong>Visits Management</strong>: This section provides an overview of patient visits, including day and night visits, seasonal trends, and other relevant metrics.</div>', unsafe_allow_html=True)
    with col2:
        st.image("undraw_World_re_768g.png", caption='Eden Care Medical', use_column_width=True)
    
    cols1, cols2 = st.columns((2))
    with cols2:
        st.markdown('<h2 class="subheader">CLAIMS MANAGEMENT</h2>', unsafe_allow_html=True)
        st.markdown('<div class="text"><strong>Claims</strong>: This section offers insights into the claims process, including claim processing times, approval rates, and other key performance indicators.</div>', unsafe_allow_html=True)
    with cols1:
        st.image("undraw_Working_re_ddwy.png", caption='Eden Care Medical', use_column_width=True)

    cl1, cl2 = st.columns((2))
    with cl1:
        st.markdown('<h2 class="subheader">PREAUTHORIZATION REQUESTS MANAGEMENT</h2>', unsafe_allow_html=True)
        st.markdown('<div class="text"><strong>Preauthorization</strong>: This section focuses on the preauthorization process, including request volumes, approval rates, and processing times.</div>', unsafe_allow_html=True)
    with cl2:
        st.image("undraw_mobile_development_re_wwsn.svg", caption='Eden Care Medical', use_column_width=True)

    # Navigation
    st.markdown('<h2 class="subheader">Navigation</h2>', unsafe_allow_html=True)
    st.markdown('<div class="text">Use the sidebar to navigate to the different sections of the dashboard:</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-item">- <strong>Visits</strong>: Analyze patient visit data.</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-item">- <strong>Claims</strong>: Explore claims processing metrics.</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-item">- <strong>Preauthorization</strong>: Review preauthorization request data.</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()