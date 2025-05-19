import requests
import re

API_KEY = "xxx"

def verify_place(place_B):
    #conditions for invalid city names- misspelled, incorrect, country...
    place_B = place_B.removeprefix(" ")
    place_B = place_B.title()

    api_url = f"http://api.openweathermap.org/data/2.5/forecast?q={place_B}&appid={API_KEY}"
    api_response = requests.get(api_url)
    print(f"\n\n{api_response.status_code}\n\n")

    if api_response.status_code == 404:
        return False
    
    if not(re.search(r"^[A-Za-z]",place_B)):
        return False    
    
    if place_B == "":
        return False
    
    else:
        return True


def get_data(place_A, forecast_time_A, type_A):
    """
    return SkyConditions data. If temperature is the SkyConditions, then obtain 
    temperature data for the next number of days indicated by forecast time.
    If SkyCondition is selected- show an icon indicating the weather SkyConditions:
    sunny, cloudy, ...
    """
    #dictionary that will be returned with elements in the list elements
    #list elements below that will be populated in the dictionary
    #that will be returned
    display_data = {"temps":[],"conditions":[],"dates":[]}
    temptr_list = []
    cloudy_ornot = []
    date_times = []

    #API to obtain that raw data
    api_url = f"http://api.openweathermap.org/data/2.5/forecast?q={place_A}&appid={API_KEY}"

    api_response = requests.get(api_url)
    api_content = api_response.json()

    filtered_api = api_content['list']
    
    num_periods = forecast_time_A*8
    #limit the data in list to the number of periods for the days input in
    #the method parameter
    filtered_api = filtered_api[:num_periods]
    

    for data in filtered_api:
        
        dates = data['dt_txt']
        date_times.append(dates)

        if type_A == "Temperature":
            #access the API key 'list' containing the data related to the weather
            
            #for loop to iterate through each list element- dictionary containing 
            #keys and values for the data that we're looking for
            #temperature list for temperatures in each period, in Kelvin
            
            tempK = data['main']['temp']
            tempC = round((tempK - 273.15),2)
            temptr_list.append(tempC)

        if type_A == "Sky Condition":
            cloudy_ornot.append(data['weather'][0]['main'])

    display_data["temps"] = temptr_list
    display_data["dates"] = date_times
    
    display_data["conditions"] = cloudy_ornot

    return display_data

if __name__ == "__main__":
    Real_city = verify_place("Gbltx")
    data = get_data(place_A="Gbltx", forecast_time_A=3, type_A="SkyCondition")
    
    