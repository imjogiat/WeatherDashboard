import streamlit as st
import plotly.express as px
import pandas as pd


def get_data(d):
    dates = pd.date_range("2024-01-01","2024-01-30")

#temperatures are temporarily a defined list- will obtain them from the API later
    temperatures = range(10,40)
    temperatures = [(d * i) for i in temperatures]

    return dates, temperatures


st.title("Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecasted Days: ", min_value=1, max_value=5,
                 help= "select the number of forecasted days")

option = st.selectbox("Select data to view",options=["Temperature", "Sky condition"])

st.subheader(f"{option} for the next {days} days in {place}")


#first create a plotly figure using plotly then use it as parameter for st.plotlychart()
#x is horiz data, y is corresponding value data, labels are axis labels
#x and y take array type (list, tuple, DF column/series, ...)

dates, temperatures = get_data(days)

figure = px.line(x=dates, y=temperatures, labels={"x":"Date", "y":"Temperature (C)"})
st.plotly_chart(figure)