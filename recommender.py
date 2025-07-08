import streamlit as st
import pickle
import pandas as pd
import numpy as np

# ✅ Page Configuration
st.set_page_config(page_title="🏡 Property Recommender", layout="wide")

# ✅ Load Data
location_df = pickle.load(open('dataset/location_distance.pkl', 'rb'))
cosine_sim1 = pickle.load(open('dataset/cosine_sim1.pkl', 'rb'))
cosine_sim2 = pickle.load(open('dataset/cosine_sim2.pkl', 'rb'))
cosine_sim3 = pickle.load(open('dataset/cosine_sim3.pkl', 'rb'))

# ✅ Recommendation Function
def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]
    top_properties = location_df.index[top_indices].tolist()

    recommendations_df = pd.DataFrame({
        '🏘️ Property Name': top_properties,
        '🔍 Similarity Score': [round(score, 3) for score in top_scores]
    })
    return recommendations_df

# --------------------------- UI --------------------------- #

st.markdown("<h1 style='text-align: center; color: #2E86C1;'>📍 Location Radius Filter</h1>", unsafe_allow_html=True)
st.markdown("---")

# ✅ Location & Radius Filter
col1, col2 = st.columns(2)
with col1:
    selected_location = st.selectbox('📌 Select a Location:', sorted(location_df.columns.to_list()))
with col2:
    radius = st.number_input('📏 Enter Radius in KMs:', min_value=1, max_value=100, value=5)

if st.button('🔎 Show Nearby Properties'):
    st.markdown("### 🏡 Properties Within Radius")
    result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()

    if result_ser.empty:
        st.warning("🚫 No properties found within the selected radius.")
    else:
        for key, value in result_ser.items():
            st.markdown(f"✅ **{key}** — {round(value / 1000)} km")

st.markdown("---")
st.markdown("<h1 style='text-align: center; color: #28B463;'>✨ Recommended Properties</h1>", unsafe_allow_html=True)

# ✅ Appartment Selector
selected_appartment = st.selectbox('🏢 Select an Appartment:', sorted(location_df.index.to_list()))

if st.button('💡 Recommend Similar Appartments'):
    recommendation_df = recommend_properties_with_scores(selected_appartment)
    st.markdown("### 🔝 Top 5 Similar Appartments")
    st.dataframe(recommendation_df.style.format({'🔍 Similarity Score': '{:.3f}'}).highlight_max(color='lightgreen', axis=0), use_container_width=True)
