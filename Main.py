import requests
import time
#from bs4 import BeautifulSoup

lista = []
## Gerador de palavras
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for letra in letras:
    for letra2 in letras:
        for letra3 in letras:
            for letra4 in letras:
                for letra5 in letras:
                    palavra = letra + letra2 + letra3 + letra4 + letra5
                    print(palavra)
## Web scrapper
# URL to scrape
                    url = (f'https://www.dicio.com.br/{palavra}/')

                    # Fetch the webpage
                    response = requests.get(url)

                    # Check if the request was successful
                    if response.status_code == 200:
                        # Parse the HTML content
                        lista.append(palavra)
                        print(f"A palavra {palavra} existe")
                    else:
                        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
                    time.sleep(0.5)
print(lista)