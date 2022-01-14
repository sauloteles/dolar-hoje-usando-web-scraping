import requests
from bs4 import BeautifulSoup

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61'}

page = requests.get('https://www.melhorcambio.com/dolar-hoje',headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')



valor_dolar = soup.find_all('td', class_='tdvalor')[2]

valor_dolar = valor_dolar.text[:6]
print(f'valor do dólar hoje: {valor_dolar}')