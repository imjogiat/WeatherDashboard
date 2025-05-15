import streamlit as st

st.title("Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecasted Days: ", min_value=1, max_value=5,
                 help= "select the number of forecasted days")

option = st.selectbox("Select data to view",options=["Temperature", "Sky condition"])

st.subheader(f"{option} for the next {days} days in {place}")