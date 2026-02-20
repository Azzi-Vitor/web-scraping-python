

# Web Scrapping para pegar apenas as frases dos famosos do site: quotes.toscrape.com

# importar Biblioteca REQUESTS pra obter código HTML da página que vamos acessar
import requests

# importar BeatifulSoup que vai transformar HTML em objeto python
from bs4 import BeautifulSoup

# buscar conteudo da página que quero coletar dados
pagina = requests.get('https://quotes.toscrape.com/')

# tratar código
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

print(dados_pagina.prettify())

# agora encontrar na página aonde que fica os dados que quero pegar

todas_frases = dados_pagina.find_all('div', class_="quote")

# utilizar laço for para percorrer todos os elementos
for div in todas_frases:
    texto = div.find('span', class_="text").text
    print(texto)

# assim seleciono apenas as frases exatas do site
