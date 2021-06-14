import requests


def weather(city_name):
    API_KEY = "9aafb81e86e4ec606536ec504377a53d"
    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (city_name, API_KEY)
    res = requests.get(url)
    data = dict(res.json())
    
    if data["cod"] == "404":
        return None
    
    temp = float(data["main"]["temp"])
    temp_celcius = int(temp - 273.15)
    
    return temp_celcius
