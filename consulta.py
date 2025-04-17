from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

cidade = input("Digite o nome da cidade a ser consultada: ")

url_base = "http://api.openweathermap.org/data/2.5/weather"

url = f"{url_base}?q={cidade}&appid={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(f"clima em {cidade}:")
    print(f"temperatura: {dados['main']['temp']}°C")
    print(f"condicao: {dados['weather'][0]['description']}")
    print(f"velocidade do vento: {dados['wind']['speed']}m/s")
    print(f"humidade: {dados['main']['humidity']}%")
else:
    print("erro ao buscar dados da API")
    
    
    
