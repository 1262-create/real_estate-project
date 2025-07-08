import streamlit as st
from streamlit_lottie import st_lottie
import json

# Set page config
st.set_page_config(
    page_title="Gurgaon Real Estate App",
    page_icon="🏙️",
    layout="centered"
)

# Load Lottie from local file
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load local animation
lottie_home = load_lottiefile("realestate.json")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏠 Gurgaon Real Estate Analytics App</h1>", unsafe_allow_html=True)

# Show animation
st_lottie(lottie_home, height=300, key="home-anim")

# Overview text
st.markdown(
    """
    <div style='text-align: center; font-size: 18px; margin-top: 20px;'>
        Welcome to your one-stop platform to explore property prices, gain data insights, and find similar properties in Gurgaon.
    </div>
    """,
    unsafe_allow_html=True
)

# Feature highlights
st.markdown("### 🔍 What This App Offers")

st.info("🔮 **Price Predictor**\n\nEstimate the price of a property based on key inputs like area, bedrooms, furnishing type, and more.")

st.success("📊 **Analytics Dashboard**\n\nExplore visualizations like word clouds, scatter plots, sector pricing maps, and more.")

st.warning("🏡 **Recommender System**\n\nEnter a location and get 5 similar properties based on your choice.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 16px;'>
        👉 Use the <strong>sidebar</strong> to explore each section of the app.
    </div>
    """,
    unsafe_allow_html=True
)


