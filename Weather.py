api_key = "5195f0cae6c8ad700ae7e191b78b4f07"
city = input("enter your city:")
#pip install requwsts
import requests
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)
data = response.json()
#print(data)
print(data['weather'][0]['description'])
print(int(data["main"]["temp"]- 273),"degree")
