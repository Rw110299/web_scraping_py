import requests
from bs4 import BeautifulSoup

def main():
    # URL que será feita a raspagem
    url = "https://www.example.com"

    # Cabeçalho para simular um navegador real e evitar bloqueios simples
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }

    try:
        # 1. Fazer a requisição HTTP para baixar o conteúdo da página
        response = requests.get(url, headers=headers)

        # 2. Verificar se a requisição foi bem-sucedida
        response.raise_for_status()  # Lança erro se status != 200

        # 3. Parsear o HTML com BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # 4. Extrair o título da página
        titulo = soup.title.string if soup.title else "Sem título"

        print(f"Título da página: {titulo}")

        # 5. Extrair todos os links da página
        print("\nLinks encontrados na página:")
        links = soup.find_all("a")

        for link in links:
            href = link.get("href")
            texto = link.get_text(strip=True)
            if href:
                print(f"Texto: {texto} | URL: {href}")

    except requests.exceptions.RequestException as e:
        print("Erro ao fazer requisição HTTP:", e)

if __name__ == "__main__":
    main()
