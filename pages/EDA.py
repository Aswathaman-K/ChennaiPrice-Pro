import streamlit as st
import pandas as pd

st.set_page_config(page_title="ChennaiPrice Pro", layout='wide', initial_sidebar_state='collapsed')
st.title("Exploratory Data Analysis")

st.header("Data used for Training", divider=True)
DataFrame = pd.read_csv(r"df_clean.csv", index_col=0)
st.dataframe(DataFrame)

st.header("Distribution Of Properties", divider=True)
left, right = st.columns(2)
with left:
    st.image("static/distribution.png", caption="Distribution by Geographic Area")
with right:
    st.image("static/distribution_by_build.png", caption="Distribution by Geographic Area & Building Type")
    
st.header("Correlation Heatmap", divider=True)
st.image("static/heatmap.png", caption="Correlation Heatmap", width=700)

st.header("Segment Share Analysis")
st.image("static/segment_share.png", caption='Distribution of Categorical Data', width=800)

st.header("How Geographical Area Affects Price", divider=True)
left, right = st.columns(2)
with left:
    st.image('static\\area_vs_price.png', caption='Price of Properties, by Geographic Area & Building Type')
with right:
    st.image('static\\area_vs_price_2.png', caption='Price of Properties, by Geographic Area & Sale Type')
    
st.image('static\\age_vs_price.png', caption='Average Price of Properties vs Property Age')

one, two, three, four, five = st.columns(5)
with five:
    if st.button("Back Home", type='primary'):
        st.switch_page('Home.py')
