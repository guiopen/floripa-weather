# floripa-weather
A small api + frontend that displays the temperature and wind speed of Florianópolis. This project was created as a technical challenge for internship. Below are the step-by-step instructions to run it along with the project documentation.

### How to run
1 - Install the necessary python modules **flask** and **requests**, you can install them with 'pip install flask' and 'pip install requests'

2 - Download this repository, open the file **floripa_weather_api.py** and put your api key in the **api_key** variable, replacing the field **'<INSERT YOUR API KEY HERE>'**. You can get your key from: https://rapidapi.com/KirylBokiy/api/openweather43/

3 - execute the file '**floripa_weather_api.py**' with the command 'python3 floripa_weather_api.py', this will run the the website on your local machine.

4 - To enter the website, open your browser and enter this adress on the search bar: **http://127.0.0.1:5000**


### Documentation:
The program is divided in three parts: the **CityWeather** class responsible for the OpenWeather api consumption and program logic, the main file **floripa_weather_api.py** responable for creating the api and starting the server and the **frontend.py** file that is responsable for consuming the **floripa_weather_api.py** and display information in a not-so-bad interface.

The **CityWeather** class receive the city name and the api key as mandatory parameters

