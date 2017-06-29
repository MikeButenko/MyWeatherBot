import requests

token = 'your token'

def get_weather():
	url = 'http://api.openweathermap.org/data/2.5/forecast?id=709930&APPID='+ token
	response = requests.get(url).json()
	city = response['city']['name']
	temp = int(response['list'][0]['main']['temp'] - 273)
	description = response['list'][0]['weather'][0]['description']
	description_day = response['list'][0]['weather'][0]['main']
	weather = 'Город - '+ city + '\n' +'Температура - '+ str(temp) + ' ' +  'градусов'+ '\n' +'Возможные погодные условия сейчас - '+ description+ '\n' +'Возможные погодные условия на весь день - '+ description_day
	return weather




