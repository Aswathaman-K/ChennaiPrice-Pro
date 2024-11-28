import streamlit as st

st.set_page_config(page_title="ChennaiPrice Pro", initial_sidebar_state='collapsed')
st.sidebar.write("")
st.sidebar.markdown("---")
st.sidebar.title("About the Creator")
st.sidebar.info(
        """
        **Developed by Aswathaman K**  
        Reach out to me:
        - 💼 [LinkedIn](https://www.linkedin.com/in/aswathaman-kumaran-2128b028a)
        - 📂 [GitHub](https://github.com/Aswathaman-K)
        """)
st.sidebar.markdown("---")

st.title("ChennaiPrice :red[Pro]")
st.header("About", divider=True)
st.write("""
This project is a machine learning-based solution to estimate house prices in Chennai, using the powerful XGBoost algorithm. The goal is to provide accurate price predictions based on various property attributes such as area, interior size, property age, proximity to main roads, number of bedrooms, and more.  

Through extensive exploratory data analysis (EDA) and data visualization, the project identifies key trends and relationships in the dataset, such as the influence of location, amenities, and quality ratings on property values. The XGBoost model is carefully tuned to achieve high prediction accuracy by leveraging its ability to handle complex interactions between features and manage missing data efficiently.  

The project is deployed as a web application using Streamlit, allowing users to interactively input property details and receive real-time price estimates. This makes it a practical tool for homebuyers, real estate agents, and property developers, showcasing the power of machine learning in solving real-world problems with precision and accessibility.""")
    
st.header("Why ChennaiPrice :red[Pro]", divider=True)
st.write("""
Property pricing is a critical aspect of real estate. Accurate predictions empower buyers, sellers, and realtors to make data-driven decisions. 
This application utilizes advanced machine learning algorithm to predict property prices in Chennai based on various features, ensuring accuracy and efficiency.
""")

st.write("")
st.subheader("Try Now!")  
left, right = st.columns(2)
with left:
    st.write("Click below to try ChennaiPrice :red[Pro] now.")      
    if st.button("Predict Now", type='primary'):
        st.switch_page("pages/Predict.py")
with right:
    st.write("Or click below to view EDA")
    if st.button("EDA", type='primary'):
        st.switch_page("pages/EDA.py")
