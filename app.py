import streamlit as st

st.set_page_config(page_title="Centralized App Hub", layout="wide")

st.title("🌐 Centralized Hub for Real Estate and Analysis Tools")
st.write("""
Welcome to the centralized hub! Use the links below to access the tools and datasets:
""")

# Links to apps
st.header("🛠️ Applications")
st.write("""
1. [CrewAI Real Estate Tool](https://crewaitool-uzwk38yjho9ouwokcjws7k.streamlit.app/)
2. [Trivandrum Plot Price Prediction-model](https://augmenteddataplotpricepred-kc4ascraaeabldkyf467ft.streamlit.app/)

""")

# Links to datasets
st.header("📂 Datasets")
st.write("""
- [Dataset 1: Property Data](https://raw.githubusercontent.com/Kirankkt/Centralized-Access-Hub/refs/heads/main/Hplot_df_filer_cleaned_no_outliers.csv)
- [Dataset 2: Plot Data](https://raw.githubusercontent.com/Kirankkt/Centralized-Access-Hub/refs/heads/main/standardized_locations_dataset.csv)
""")

st.info("Bookmark this page for quick access to all tools and data!")

# Footer or additional notes
st.markdown("""
---
This hub is maintained to provide quick and easy access to the tools and data for our real estate business. 
For any issues or updates, contact the admin.
""")
