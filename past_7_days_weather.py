import requests
from datetime import date,datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

#function for fetching latitude & longitude of any place
def get_lat_long(place):
    url=f"https://geocoding-api.open-meteo.com/v1/search?name={place}"
    response=requests.get(url)
    result=response.json()

    if "results" not in result or len(result["results"]) == 0:
        raise ValueError("City not found. Please check spelling.")
    
    lat=result["results"][0]["latitude"]
    lon=result["results"][0]["longitude"]
    return lat, lon
#-----------------------------------------------------------------------

#function for fetching 7 days weather for any place
def get_7_days_weather(place,start_date,end_date):
    lat,lon=get_lat_long(place)
    url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&start_date={start_date:%Y-%m-%d}&end_date={end_date:%Y-%m-%d}&daily=temperature_2m_max,temperature_2m_min"
    response=requests.get(url)
    data=response.json()
    return data
#------------------------------------------------------------------------

# using pandas for data framing
def data_frame(daily_data):
    df=pd.DataFrame({
        "date": daily_data["time"],
        "max_temp": daily_data["temperature_2m_max"],
        "min_temp": daily_data["temperature_2m_min"]
    })
    #convert date strings to datetime
    df["date"]=pd.to_datetime(df["date"])
    return df
#--------------------------------------------------------------------------

#visualizing the generated data
def graph(df,location):
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
    plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')
    
    #plt.bar(df['date'], df['max_temp'],width=0.4, label='Max Temp')
    #plt.bar(df['date'], df['min_temp'],width=0.4, label='Min Temp')

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f'{location} Weather - Past 7 Days')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Rotate x-axis labels for readability
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot
    plt.savefig('weather_chart.png')
    plt.show()
    pass
#-------------------------------------------------------------------------

#Saving to CSV
def save_as_csv(df,location):
    # Create data folder if it doesn't exist
    location = location.lower()
    if not os.path.exists('data'):
        os.makedirs('data')

    # Save to CSV
    df.to_csv(f'data/{location}.csv', index=False)
    print(f"Data saved to data/{location}.csv")
    pass
#-----------------------------------------------------------------------------

# main method
def main():
    # fetch current date and a week ago date
    today=date.today()
    week_ago=today-timedelta(days=6) # days=6 since start date & end date both included
    n=1
    while n!=0:
        
        city=input("Enter your city: ")
        result=get_7_days_weather(place=city,start_date=week_ago,end_date=today)
        result=result['daily']
        final_data=data_frame(result) ##calling data framing function
        print(f"The past 7 days weather for {city} is: ")
        print(final_data)
        graph(df=final_data,location=city) ##calling graph plotting function
        save_as_csv(df=final_data,location=city) ##calling save as CSV function
        n=int(input("To continue press 1 else press 0: "))
#-----------------------------------------------------------------------------

if __name__=="__main__":
    main()