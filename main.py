import streamlit as st
import plotly.express as px
import pandas as pd
import backend


st.title("Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecasted Days: ", min_value=1, max_value=5,
                 help= "select the number of forecasted days")

weather_type = st.selectbox("Select data to view",options=["Temperature", "Sky Condition"])

st.subheader(f"{weather_type} for the next {days} days in {place}")


#first create a plotly figure using plotly then use it as parameter for st.plotlychart()
#x is horiz data, y is corresponding value data, labels are axis labels
#x and y take array type (list, tuple, DF column/series, ...)
# place = "Dublin"
# days = 4
# weather_type = "Temperature"
real_place = backend.verify_place(place_B=place)

if real_place == False:
    place_msg = """Invalid or missing city name. Please verify the spelling of the city
    name or verify if the city is a real place. Please verify that it is not 
    a Country, Province, State or Region name.
"""
    st.write(place_msg)

else:
    weather_data = backend.get_data(place_A=place, forecast_time_A=days, type_A=weather_type)

    #obtain data from dictionary from get_data and input to x, y
    if weather_type == "Temperature":
        figure = px.line(x=weather_data['dates'], y=weather_data['temps'], labels={"x":"Date", "y":"Temperature (C)"})
        st.plotly_chart(figure)


    if weather_type == "Sky Condition":
        # weather_data['conditions']
        col_list = st.columns(8)
        print(col_list)

        for i,condition in enumerate(weather_data["conditions"]):

            match condition:
                case "Clouds":
                    # weather_data['conditions']
                    col_list[i%8].image(r"condition_images\cloud.png")
                    
                case "Clear":
                    col_list[i%8].image(r"condition_images\clear.png")
                    
                case "Rain":
                    col_list[i%8].image(r"condition_images\rain.png")

                case "Snow":
                    col_list[i%8].image(r"condition_images\snow.png")

    