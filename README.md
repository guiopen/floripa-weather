## floripa-weather
A small api + frontend that displays the temperature and wind speed of Florianópolis. This project was created as a technical challenge for internship. Below are the step-by-step instructions to run it along with the project documentation.

### How to run:
1 - Install the necessary python modules **flask** and **requests**, you can install them with 'pip install flask' and 'pip install requests'

2 - Download this repository, open the file **floripa_weather_api.py** and put your api key in the **api_key** variable, replacing the field **'<INSERT YOUR API KEY HERE>'**. You can get your key from: https://rapidapi.com/KirylBokiy/api/openweather43/

3 - Execute the file '**floripa_weather_api.py**' with the command 'python3 floripa_weather_api.py', this will run the the website on your local machine.

4 - To access the website, open your browser and enter this address on the search bar: **http://127.0.0.1:5000**


![floripa_weather](https://github.com/guiopen/floripa-weather/assets/94094527/7a05f2da-3d2e-49fd-9fd3-192a524da0f6)


### Documentation:
The program is divided in three parts: the **CityWeather** class responsible for the OpenWeather api consumption and program logic, the main file **floripa_weather_api.py** responsible for creating the api and starting the server and the **frontend.py** file that is responsible for consuming the **floripa_weather_api.py** and display information in a not-so-bad interface. 

#### Program Logic
The **CityWeather** class receives the city name and the api key as mandatory parameters and attributes, it also has a self.__full_data attribute that contains complete weather data, obtained with the **get_openweather_data()** method, which consumes the OpenWeather api and returns a dictionary with extensive weather info for the next five days, measured every 3 hours and doesnt need any parameters. There are two more important methods, **get_temperatures()** receives an integer X as a mandatory parameter and returns a dictionary with the same amount of temperatures as X and their mean, in celsius. The other method is **get_wind()** that receives a Y amount of hours as mandatory parameters and a speed unit (mps or kmh) as an optional parameter, it will return a string with the average wind of the next Y hours.

#### API
In the **floripa_weather_api.py** we utilizes the Flask framework and the CityWeather class to create two api routes with Florianópolis data. The first route ('/temps') uses the get_temperatures() method to return a json with the next 4 temperatures of floripa and their mean. The second route ('/wind') uses the get_wind() method to return a json with floripa average wind for the next 24 hours. This is the file that we use to initialize the website, it will create a localhost at http://127.0.0.1:5000 and also provide the frontend at the same adress.

#### Frontend
In the **frontend.html** file the idea was to create something that resambles the weather, so I decided to use a solid blue background to represent the sky and in the middle a yellow square with rounded corners to represent the sun. The floripa_weather_api consumption was made with javascript fetch() and the results displayed on the 'sun'.
