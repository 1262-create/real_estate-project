import streamlit as st
import pandas as pd
import numpy as np
import pickle as p

st.set_page_config(page_title='abc', page_icon="🏠")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏡 Property Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("---")

with open('df.pkl','rb') as f:
    df = p.load(f)

with open('pipeline.pkl', 'rb') as file:
    pipeline = p.load(file)

    st.subheader('🔽 Please fill the property details:')

    property_type = st.selectbox('🏙️ Property Type', ['flat', 'house'])
    sector = st.selectbox('📍 Sector', sorted(df['sector'].unique().tolist()))
    bedrooms = float(st.selectbox('🛏️ Number of Bedrooms', sorted(df['bedRoom'].unique().tolist())))
    bathroom = float(st.selectbox('🛁 Number of Bathrooms', sorted(df['bathroom'].unique().tolist())))
    balcony = st.selectbox('🌿 Number of Balconies', sorted(df['balcony'].unique().tolist()))
    property_age = st.selectbox('⏳ Property Age', sorted(df['agePossession'].unique().tolist()))
    built_up_area = float(st.number_input('📐 Built Up Area (in sq ft)'))

    servant_room = float(st.selectbox('🧹 Servant Room', [0.0, 1.0]))
    store_room = float(st.selectbox('📦 Store Room', [0.0, 1.0]))

    furnishing_type = st.selectbox('🛋️ Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
    luxury_category = st.selectbox('💎 Luxury Category', sorted(df['luxury_category'].unique().tolist()))
    floor_category = st.selectbox('🏢 Floor Category', sorted(df['floor_category'].unique().tolist()))

if st.button('🔍 Predict Price'):

    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area,
             servant_room, store_room, furnishing_type, luxury_category, floor_category]]

    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    one_df = pd.DataFrame(data, columns=columns)

    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    st.success("✅ Estimated Price Range:")
    st.markdown(f"<h3 style='color: #2196F3;'>₹ {round(low, 2)} Cr &nbsp; - &nbsp; ₹ {round(high, 2)} Cr</h3>", unsafe_allow_html=True)
    st.balloons()
