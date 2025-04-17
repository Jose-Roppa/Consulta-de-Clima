from dotenv import load_dotenv
import os
import requests

#carrega as variaveis de ambiente
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

#solicita o nome da cidade ao usuario
cidade = input("Digite o nome da cidade a ser consultada: ")

#define a url da api
url_base = "http://api.openweathermap.org/data/2.5/weather"
url = f"{url_base}?q={cidade}&appid={API_KEY}"

#faz a requisicao na api
response = requests.get(url)

#verifica se a requisicao foi bem sucedida
if response.status_code == 200:
    #converte a resposta em json
    dados = response.json()
    #exibe os dados
    print(f"clima em {cidade}:")
    print(f"temperatura: {dados['main']['temp']-273.15}°C")#converte a temperatura de Kelvin para celsius
    print(f"condicao: {dados['weather'][0]['description']}")
    print(f"velocidade do vento: {dados['wind']['speed']}m/s")
    print(f"humidade: {dados['main']['humidity']}%")
else:
    #exibe uma mensagem de erro caso a requisicao nao seja bem sucedida
    print("erro ao buscar dados da API")

    
