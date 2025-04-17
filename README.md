# Consulta de Clima

Projeto de consulta de clima utilizando a API do OpenWeatherMap.

## Descrição

O **Consulta de Clima** é uma aplicação simples desenvolvida em Python que permite ao usuário consultar informações climáticas de qualquer cidade do mundo. O programa solicita o nome da cidade e retorna dados como:

- Temperatura atual
- Condições climáticas (ex: céu limpo, nublado, chuva)
- Velocidade do vento
- Umidade do ar

A aplicação utiliza a API pública do [OpenWeatherMap](https://openweathermap.org/api) para obter os dados em tempo real.

## Requisitos

- Python 3.x
- Conta gratuita na OpenWeatherMap para obter uma chave de API
- Bibliotecas listadas em `requirements.txt`

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/Consulta-de-Clima.git
   cd Consulta-de-Clima
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure sua chave de API:**
   - Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave:
     ```
     OPENWEATHER_API_KEY=sua_chave_aqui
     ```

## Uso

Execute o script principal:

```bash
python main.py
```

Siga as instruções na tela para digitar o nome da cidade desejada.

## Exemplo

```
Digite o nome da cidade: São Paulo
Temperatura: 25°C
Condições: Céu limpo
Velocidade do vento: 10 km/h
Umidade: 60%
```

## Estrutura do Projeto

```
Consulta-de-Clima/
├── main.py
├── requirements.txt
├── README.md
└── .env (não versionado)
```

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork este repositório
2. Crie uma branch (`git checkout -b feature/sua-feature`)
3. Commit suas alterações (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/sua-feature`)
5. Abra um Pull Request
