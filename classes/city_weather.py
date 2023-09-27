import requests


class CityWeather:
    def __init__(self, city: str, api_key: str) -> None:
        if isinstance(city, str):
            self.__city = city
        else:
            raise ValueError('city parameter must be a string')
        if isinstance(api_key, str):
            self.__api_key = api_key
        else:
            raise ValueError('api_key parameter must be a string')
        self.__full_data = self.get_openweather_data()
    
    #consume openweather api to get complete weather data for the next 5 days
    def get_openweather_data(self) -> dict:
        url = 'https://openweather43.p.rapidapi.com/forecast'
        appid = 'da0f9c8d90bde7e619c3ec47766a42f4'
        querystring = {'q':self.__city,'appid':appid,'units':'metric'}
        headers = {'X-RapidAPI-Key': self.__api_key, 'X-RapidAPI-Host': 'openweather43.p.rapidapi.com'}
        return requests.get(url, headers=headers, params=querystring).json()

    #return the next X temperatures measured every 3 hours and their mean
    def get_temperatures(self, amount: int) -> dict:
        temps = [round(temperature['main']['temp'],1) for temperature in self.__full_data['list'][:amount]]
        response = {'total_temps': temps,
                    'mean_temps': round(sum(temps)/amount, 1)}
        return response
    
    #return the mean of wind speed in the next X hours approximately, speed unit can be either kmh or ms
    def get_wind(self, next_hours: int, speed_unit: str='kmh') -> str:
        amount = int(next_hours / 3)
        wind_mean = 0
        for wind_speed in self.__full_data['list'][:amount]:
            wind_mean += wind_speed['wind']['speed']
        wind_mean = wind_mean / amount
        if speed_unit == 'kmh':
            return str(round(wind_mean * 3.6, 1))
        elif speed_unit == 'ms':
            return str(round(wind_mean, 1))
        else:
            ValueError('speed_unit parameter should be either kmh or ms')

    @property
    def city(self) -> str:
        return self.__city
    @city.setter
    def city(self, city) -> None:
        if isinstance(city, str):
            self.__city = city

    @property
    def api_key(self) -> str:
        return self.__api_key
    @api_key.setter
    def api_key(self, api_key) -> None:
        if isinstance(api_key, str):
            self.__api_key = api_key
       
    @property
    def full_data(self) -> dict:
        return self.__full_data
