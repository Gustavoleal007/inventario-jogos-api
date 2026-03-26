import requests

url = "http://127.0.0.1:5000/jogos"

dados = {
    "nome": "FIFA 24",
    "genero": "Esporte",
    "plataforma": "PC",
    "preco": 299.90,
    "estoque": 10
}

resposta = requests.post(url, json=dados)

print(resposta.status_code)
print(resposta.json())