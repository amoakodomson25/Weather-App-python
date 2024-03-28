import requests

apiKey = 'df94f4b70075c51b04f1bef2e1d29073'

userInput = input("Enter City: ") 
weather_data =  requests.get(
     f"https://api.openweathermap.org/data/2.5/weather?q={userInput}&units=imperial&APPID={apiKey}")


if weather_data.json()['cod'] == '404':
    print("No city found")
    print()
else:
    weather = weather_data.json()['weather'][0]['main']
    temp_f = round(weather_data.json()['main']['temp'])
    temp_c = round((temp_f - 32) * (5/9))
    print("------------------------------------------------------------------------------")
    print(f"The temperature in {userInput} is: {temp_f}°F or {temp_c}°C, and there would be {weather}.")
    print("------------------------------------------------------------------------------")
    print()

