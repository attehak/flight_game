import requests

def get_weather(city):
    if not city:
        return "Säätietoja ei saada(404)."
    
    api_key = "c43c31672d95a9d9da6f099812e37a32" 

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=fi"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            desc = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"Sää kohteessa {city}: {desc}, lämpötila {temp}°C."
        elif response.status_code == 404:
             return f"Säätietoja ei löytynyt kaupungille {city}."
        else:
            return "Säätietoja ei voitu hakea juuri nyt."
    except Exception as e:
        return "Yhteysvirhe sääpalveluun."