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
    temp = round(weather_data.json()['main']['temp'])
    print("------------------------------------------------------------------------------")
    print(f"The temperature in {userInput} is: {temp}°F, hence the weather is {weather}.")
    print("------------------------------------------------------------------------------")
    print()

