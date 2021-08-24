#I used flask as my python web framework
from flask import Flask, render_template, request
import pullingWeatherInfo

app = Flask(__name__)


@app.route('/getWeather' )
def collect_info():
	#this function collects the phone_number and city
	phone = request.args.get("phone")
	city  = request.args.get("city")

	#defaults to my home data
	if not phone: phone = "+16175993645"
	if not city: city = "Cambridge"

	#pull the message with weather info
	msg = pullingWeatherInfo.get_weather(city)

	#get the bool if the message was sent
	success = pullingWeatherInfo.send_message(phone, msg)
	if success:
		#redirect to diff html pages
		template_file = 'success.html'
	else:
		template_file = 'failure.html'
	return render_template(template_file)





@app.route('/')
def send_form():
	return render_template('mainPage.html')


if __name__ == '__main__':
	app.run(debug=True)