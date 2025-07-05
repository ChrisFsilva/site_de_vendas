from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

url = 'https://gratuitos.netlify.app/'
page =  requests.get(url)
html = page.text

soup = BeautifulSoup(html,'html.parser')

title = soup.find('title').text

cursos = []

for line in soup.find_all('tr'):
    dados = []
    for item in line.find_all(['th','td']):
        dados.append(item.text.strip())
    
    cursos.append(dados)

print(f'O titulo é: {title}')
print(f'A tabela é: {cursos}')
