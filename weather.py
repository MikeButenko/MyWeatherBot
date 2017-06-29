import requests

#http://sinoptik.vn.ua/api.php?city=Novomoskovsk
# openweathermap:
# Dnipro_id: 709930
# Novomoskovsk_id: 699445

token = 'b419d37ccd9921625998427345f82716'

def get_weather():
	#url = 'http://sinoptik.vn.ua/api.php?city=Novomoskovsk'
	url = 'http://api.openweathermap.org/data/2.5/forecast?id=709930&APPID='+ token
	response = requests.get(url).json()
	city = response['city']['name']
	temp = int(response['list'][0]['main']['temp'] - 273)
	description = response['list'][0]['weather'][0]['description']
	description_day = response['list'][0]['weather'][0]['main']
	weather = 'Город - '+ city + '\n' +'Температура - '+ str(temp) + ' ' +  'градусов'+ '\n' +'Возможные погодные условия сейчас - '+ description+ '\n' +'Возможные погодные условия на весь день - '+ description_day
	return weather


# get_weather()

