import requests

url = "https://api-agromonitor-production.up.railway.app/getData"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data['temperature']
    humidity = data['humidity']
    print("Dados da API:")
    print(f"Temperatura: {temperature}°C")
    print(f"Umidade: {humidity}%")
else:
    print("Falha ao obter os dados. Código de status:", response.status_code)