import requests, json
from twilio.rest import Client
import requests


#Key = 63cba1eee201bd2182f630eb700343bd


# Constants:
key = "63cba1eee201bd2182f630eb700343bd"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
AdminPhoneNumber="+18509309178"
account_sid = 'AC03ea2e28eb640deed4843d25f71631ec'
auth_token = '584f8c9cd1d2fc4c2437422d667c07a5'



def get_weather(city):
	#return a string that has the weather for the city
	url = base_url + "appid=" + key + "&q=" + city
	response = requests.get(url)
	info = response.json()
	returnValue = "The city %s was not found" % city


	if info["cod"] != "404":

		#store the main part of the variable
		main = info["main"]

		#current tempurature
		tempK = main["temp"]
		#this receives it in Kelvin so lets translate to farenheight
		#kelvin to F is
		#F=9/5(K-273)+32
		temp = round((9/5)*(tempK-273)+32, 1)

		#current pressure
		press = main["pressure"]

		#current humidity
		humidity = main["humidity"]

		#current weather
		weather = info["weather"]

		weatherDescription = weather[0]["description"]

		#print out the information we just got

		returnValue = (
			"*********************************\n" +
			"For the city of " + city + 
			"\n\nThe tempurature outside is: " + str(temp) + " F" +
			"\n\nThe pressure outside is " + str(press) + " hPa" +
			"\n\nThe humidtity outside is " + str(humidity) +  "% " +
			"\n\nAn overall description is: " + str(weatherDescription))

	return returnValue


def send_message(phone_number, message):
	#send a message to phone_number via twilio 
	#return boolean True (if sent successfully), 
	#False otherwise 
	


	returnValue = True
	try:
		client = Client(account_sid, auth_token)
		message = client.messages.create(
	    #to="+16175993645",
	    to=phone_number,
	    from_=AdminPhoneNumber,
	    body=message)
	except Exception:
		import traceback
		print("Message failed to send")
		returnValue = False

	return returnValue


if __name__ == '__main__':
	city = input("Tell me the city? ")
	phone = input("Send to what phone #? ")
	msg = get_weather(city)
	send_message(phone, msg)






