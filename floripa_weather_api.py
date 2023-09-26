from classes.city_weather import CityWeather
from flask import Flask, jsonify, render_template


#create an instace that contains floripa weather, dont forget to put your api key below
api_key = '<INSERT YOUR API KEY HERE>'
floripa = CityWeather('Florianopolis', api_key)
app = Flask(__name__)

#the first route return the next 4 temperatures in celsius and their mean. they were measured from 3 to 3 hours
@app.route('/temps')
def temps() -> dict:
    return jsonify(floripa.get_temperatures(4)) #example output: {"mean_temps":17.1,"total_temps":[17.6,17.3,16.9,16.6]}

#the second route returns the avarage wind for the next 24 hours in kilometers per hour
@app.route('/wind')
def wind() -> str:
    return jsonify(floripa.get_wind(24)) #example output: "2.7"

@app.route('/')
def render():
    return render_template('frontend.html')

if __name__ == '__main__':
    app.run()
