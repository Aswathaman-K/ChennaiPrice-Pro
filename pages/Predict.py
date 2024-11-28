import streamlit as st
import xgboost as xgb
import numpy as np

st.set_page_config(page_title="ChennaiPrice Pro", initial_sidebar_state='collapsed', page_icon='🏠')
st.title('Estimate your House Price')
st.caption('Enter the specifications and watch the estimation happen in real-time.')
area = st.selectbox(
    "Area",
    ['Aadyar', 'Anna Nagar', 'Chrompet', 'Karapakkam', 'KK Nagar', 'T Nagar', 'Velachery'],
    placeholder='Select Property Area',
    index=None
)

right, centre, left = st.columns(3)
with right:
    int_area = st.number_input('Interior Area', step=1, placeholder='Int. Area in SqFt', value=None)
with centre:
    prop_age = st.number_input('Property Age', step=1, placeholder='Age in Years', value=None)
with left:
    dist_to_main_road = st.number_input('Distance To Main Road', step=1, placeholder='Distance in Feet', value=None)
    
right, centre, left = st.columns(3)
with right:
    n_bedroom = st.number_input('Number of Bedrooms', step=1, value=None, min_value=1, max_value=4, placeholder='1-4')
with centre:
    n_bathroom = st.number_input('Number of Bathrooms', step=1, value=None, min_value=1, max_value=3, placeholder='1-3')
with left:
    n_room = st.number_input('Number of Rooms', step=1, value=None, min_value=1, max_value=10, placeholder='1-10')
    
right, left = st.columns(2)
with right:
    sale_cond = st.selectbox(
        "Sale Condition",
        ['Normal', 'Abnormal', 'Partial', 'Adjacent Land', 'Family'],
        index=None,
    )
    build_type = st.selectbox(
        "Building Type",
        ['Residential', 'Commercial', 'Others'],
        index=None,
    )
    street = st.selectbox(
        "Street Type",
        ['Paved', 'Gravel', 'No Access'],
        index=None,
    )
    
with left:
    park_facil = st.selectbox(
        "Parking Facility",
        ['Yes', 'No'],
        index=None,
    )
    util_avail = st.selectbox(
        "Available Utilities",
        ['No Sewage Water', 'Electricity Only', 'All Public Facilities'],
        index=None,
    )
    mzzone = st.selectbox(
        "Zone",
        ['Residential - Low', 'Residential - Medium', 'Residential - High', 'Industrial', 'Agricultural', 'Commertial'],
        index=None,
    )
    
right, left = st.columns(2)
with right:
    q_bed = st.slider('Bedroom Quality', min_value=1, max_value=5, value=3)
    q_bath = st.slider('Bathroom Quality', min_value=1, max_value=5, value=3)
    
with left:
    q_rooms = st.slider('Room Quality', min_value=1, max_value=5, value=3)
    q_overall = st.slider('Overall Quality', min_value=1, max_value=5, value=3)
    
'---'

def area_conv(area):
    mapping = {
        "Adayar": 0,
        "Anna Nagar": 1,
        "Chrompet": 2,
        "KK Nagar": 3,
        "Karapakkam": 4,
        "T Nagar": 5,
        "Velachery": 6
    }
    return mapping.get(area, -1)


def sale_conv(sale):
    mapping = {
        "Abnormal" : 0,
        "Adjacent Land" : 1,
        "Family" : 2,
        "Normal" : 3,
        "Partial" : 4
    }
    return mapping.get(sale, -1)
def park_conv(park):
    mapping = {
        "No" : 0,
        "Yes" : 1,
    }
    return mapping.get(park, -1)
def build_conv(build):
    mapping = {
        "Commercial" : 0,
        "Residential" : 1,
        "Others" : 2
    }
    return mapping.get(build, -1)
def util_conv(util):
    mapping = {
        "All Public Facilities" : 0,
        "Electricity Only" : 1,
        "No Sewage Water" : 2
    }
    return mapping.get(util, -1)
def street_conv(street):
    mapping = {
        "Gravel" : 0,
        "No Access" : 1,
        "Paved" : 2
    }
    return mapping.get(street, -1)
def zone_conv(zone):
    mapping = {
        "Agricultural" : 0,
        "Commercial" : 1,
        "Industrial" : 2,
        "Residential - High" : 3,
        "Residential - Low" : 4,
        "Residential - Medium" : 5,
    }
    return mapping.get(zone, -1)
    
booster = xgb.XGBRegressor()
booster.load_model('xgboost_model.json')

if all([area, int_area, prop_age, dist_to_main_road, n_bedroom, n_bathroom, n_room]):
    data = np.array([
        area_conv(area),
        int_area,
        dist_to_main_road,
        n_bedroom,
        n_bathroom,
        n_room,
        sale_conv(sale_cond),
        park_conv(park_facil),
        build_conv(build_type),
        util_conv(util_avail),
        street_conv(street),
        zone_conv(mzzone),
        q_rooms,
        q_bath,
        q_bed,
        q_overall,
        prop_age
    ]).reshape(1, -1)
    
    # Make prediction
    value = booster.predict(data)
    st.write(f"## Value Estimation: :red[Rs. {int(value)}]")
else:
    st.write("## Value Estimation: :red[Rs. 0]")
    
one, two, three, four, five = st.columns(5)
with five:
    if st.button("Back Home", type='primary'):
        st.switch_page('Home.py')

st.sidebar.write("")
st.sidebar.title("About the Creator")
st.sidebar.info(
        """
        **Developed by Aswathaman K**  
        Reach out to me:
        - 💼 [LinkedIn](https://www.linkedin.com/in/aswathaman-kumaran-2128b028a)
        - 📂 [GitHub](https://github.com/Aswathaman-K)
        """)
st.sidebar.markdown("---")
