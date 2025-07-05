from bs4 import BeautifulSoup
import requests

# Atribuir o link do site a um variavel (url)
url = 'https://chrisfsilva.github.io/site_de_vendas/'
# atribuir a coleta do site (request.get) a uma variavel (pagina)
pagina = requests.get(url)
# Atribuir o codigo do request salvo na variavel pagina a uma variavel (html)
html = pagina.text

# Alinhar o conteudo html
soup = BeautifulSoup(html, 'html.parser')

# Criando uma lista para produtos
produtos = []
# Criando uma lista para valores
valores = []

# Criando loop
    # Para cada (i) que o BeautifulSoup(soup) Localizar tudo (find_all) que esteja dentro das div's com a class = "produto"
for i in soup.find_all('div', class_='produto'):
    # Atribuir em forma de texto dentro da variavel preco tudo o que localizar nos span com a classe preco
    preco = item.find('span', class_='preco').text
    # Atribuir a variavel preco na lista valores
    valores.append(preco)
    # para cada valor da lista valores a variavel lista_valores substituirá R$ por nada
    lista_valores = [valor.replace('R$','').strip() for valor in valores]
    # para cada valor da lista_valores a variavel l substituirá R$ por nada
    l = [v.replace (',','').strip() for v in lista_valores]
    # transformar os valors de i em fload e coloca-los na varivavel dados_valores_reais
    dados_valores_reais = [float(i) for i in dados_real]

    print(lista_valores_reais)

for item2 in soup.find_all('div', class_= 'produto'):
    nome = item2.find('h2', class_ = 'nome').text
    produtos.append(nome)
print(produtos)    


# for item in soup.find_all('div',class_='produto'):
#     nome = item.find('h2', class_='nome').text
#     preco = item.find('span', class_='preco').text
#     produtos.append({
#         'nome': nome,
#         'preço': preco,
#     })

# print ('Produtos encontrados')
# for item in produtos:
#     print (f'{item['nome']} - {item['preço']}')

# print('valores encontrados')
# with open('produtos.txt','w') as arquivo:
#     for produto in produtos:
#         arquivo.write(f'{produto['nome']} - {produto['preço']},')

