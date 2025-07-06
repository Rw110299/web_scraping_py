import requests
from bs4 import BeautifulSoup

def test_status_code():
    url = "https://www.example.com"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Status code inesperado: {response.status_code}"

def test_titulo_pagina():
    url = "https://www.example.com"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    titulo = soup.title.string if soup.title else None
    assert titulo is not None, "Título da página não encontrado"
    assert len(titulo) > 0, "Título da página está vazio"
