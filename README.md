<h1 align="center">Web Scraping - Produtos e Tabelas</h1>			
<br>
<h4 align="center"> 💻 Em produção 💻 </h4>
<h3 align="center">Projeto de Web Scraping com Python para coleta de dados de cursos e produtos</h3>

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre o projeto](#-sobre-o-projeto)
     * [Problemas-resolvidos](#-problemas-resolvidos)
   * [Layout](#-layout)
   * [Como executar o projeto](#-como-executar-o-projeto)
     * [Pré-requisitos](#pré-requisitos)
     * [Funcionalidades](#funcionalidades)
   * [Tecnologias](#-tecnologias)
   * [Autor](#-autor)
   * [Licença](#-licença)
<!--te-->

## 💻 Sobre o projeto 

Descrição:  
Este projeto tem como objetivo realizar a extração automatizada de informações de duas páginas distintas utilizando Python e a biblioteca BeautifulSoup. Os dados extraídos são:

- Nome e preço de produtos em uma loja fictícia hospedada no GitHub Pages.
- Tabela com dados de cursos gratuitos extraídos de uma segunda página.

Esses dados podem ser utilizados em análises, visualizações gráficas ou armazenados em arquivos para relatórios posteriores.

---

## 🚧 Problemas resolvidos

```bash
#### 1. 🧾 Dificuldade em coletar e organizar informações de sites estáticos
  Antes: Era necessário copiar e colar manualmente os dados.
  Com o código: A coleta ocorre automaticamente via Python com BeautifulSoup.
```
```bash
#### 2. 📊 Falta de dados estruturados para visualizações e análises
  Antes: Informações de preços e cursos estavam espalhadas no HTML.
  Com o código: Os dados são organizados em listas e prontos para uso com pandas, matplotlib ou salvamento em arquivos.
```
```bash
#### 3. 🕐 Perda de tempo em tarefas repetitivas de extração
  Antes: Atualizar informações exigia acessar cada página manualmente.
  Com o código: Um script executável coleta todos os dados com apenas uma execução.
```

## 🎨Layout

- O projeto não possui uma interface gráfica, mas pode ser integrado facilmente com matplotlib, tkinter, pandas, ou armazenado em .csv/.json.


---

## 🚀 Como executar o projeto

### Pré-requisitos

- Ter o Python 3.8 ou superior instalado
- Instalar as bibliotecas:

```bash
pip install beautifulsoup4 requests
```
### Instalação:
- Clone o repositório:
```bash
git clone https://github.com/ChrisFsilva/NomeDoRepositorio.git
```

- Acesse a pasta:

```bash
cd NomeDoRepositorio
```

- Execute os scripts:

```bash
python scraping_produtos.py
python scraping_cursos.py
```
#### Funcionalidades

```bash

- scraping_produtos.py
  Extrai nomes e preços de produtos de um site estático.

- scraping_cursos.py
  Coleta dados de uma tabela HTML com informações de cursos gratuitos.

- Os dados podem ser impressos, visualizados em gráficos ou exportados para arquivos.

```

### 🧑‍💻Guia do Usuário:

``` bash
- Execute o script diretamente no terminal.
- Os resultados são exibidos na tela, podendo ser adaptados para visualização ou persistência.
```

## 🛠 Tecnologias

As seguintes tecnologias foram usadas na construção do projeto:

-   **[Python](https://www.python.org/)**
-   **[BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)**
-   **[Requests](https://pypi.org/project/requests/)**
-   **[(opcional)Matplotlib](https://matplotlib.org/)**


---

## 🦸🏻‍♂️ Autor

 <br>
  <sub><b><p>Christopher Silva</p></b></sub></a>
 <br />

[![Linkedin Badge](https://img.shields.io/badge/-Christopher%20Silva-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/chris-f-silva//)](https://www.linkedin.com/in/chris-f-silva/) 
[![Gmail Badge](https://img.shields.io/badge/-chrisspfc.silva@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:daniel.rodrigues.soarees@gmail.com)](mailto:chrisspfc.silva@gmail.com)

---

## 📝 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes. [MIT](./LICENSE)

Feito por: Christopher Silva
</div>
