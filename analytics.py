import streamlit as st
import pickle as p
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Page config (with closing quote fixed)
st.set_page_config(page_title="📊 Real Estate Analytics", layout="wide")

# ✅ Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📊 Property Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# ✅ Load data
new_df = pd.read_csv('dataset/data_viz1.csv')
with open('dataset/feature_text.pkl', 'rb') as f:
    feature_text = p.load(f)

# ✅ Geomap
group_df = new_df.groupby('sector')[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']].mean()
st.subheader("🌍 Sector Price Per Sqft Map")
fig = px.scatter_mapbox(
    group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
    color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
    mapbox_style="open-street-map", width=1200, height=700, hover_name=group_df.index
)
st.plotly_chart(fig, use_container_width=True)

# ✅ WordCloud
st.subheader("☁️ WordCloud of Property Features")
wordcloud = WordCloud(
    width=800, height=800, background_color='black',
    stopwords=set(['s']), min_font_size=10
).generate(feature_text)

fig, ax = plt.subplots(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
st.pyplot(fig)

# ✅ Scatter Plot
st.subheader("📐 Built-up Area vs Price")
property_type = st.selectbox('🏘️ Select Property Type', ['flat', 'house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="📈 House: Built-up Area vs Price")
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom", title="📈 Flat: Built-up Area vs Price")

st.plotly_chart(fig1, use_container_width=True)

# ✅ Pie Chart
st.subheader("🧁 BHK Distribution by Sector")
sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0, 'overall')
selected_sector = st.selectbox('📍 Select Sector', sector_options)

if selected_sector == 'overall':
    fig2 = px.pie(new_df, names='bedRoom', title="Overall BHK Distribution")
else:
    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom', title=f"BHK Distribution in {selected_sector}")

st.plotly_chart(fig2, use_container_width=True)

# ✅ Boxplot
st.subheader("📦 Side-by-Side BHK Price Comparison")
fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='Price Range by BHK')
st.plotly_chart(fig3, use_container_width=True)

# ✅ Distplot
st.subheader("🏠 Distribution of Property Prices by Type")
fig4 = plt.figure(figsize=(10, 4))
sns.histplot(new_df[new_df['property_type'] == 'house']['price'], kde=True, label='House', color="orange")
sns.histplot(new_df[new_df['property_type'] == 'flat']['price'], kde=True, label='Flat', color="skyblue")
plt.legend()
plt.title("Distribution of Property Prices")
st.pyplot(fig4)
