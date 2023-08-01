import requests,os
api_key = os.getenv('API-KEY')
base_url = 'http://api.openweathermap.org/data/2.5/weather'

query = input('Enter the city: ')
requests_url = f'{base_url}?appid={api_key}&q={query}'
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather']
    temperature = data['main']['temp']
    print(f'Weather: {weather}')
    print(f'Temperature: {temperature}')
else:
    print('An Error Occured')