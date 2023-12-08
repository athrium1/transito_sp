from bs4 import BeautifulSoup
import requests
import json 

# executando o request para a pagina da CET
home_request = requests.get('http://www.cetsp.com.br/')
# recuperando todas informações em forma de texto
home_content = home_request.text
     
soup = BeautifulSoup(home_content, 'html.parser')

box_dados = soup.find(class_= "boxTransito")

regioes_cidade = {'norte' : 'info norte', 'oeste' : 'info oeste', 'Centro' : 'info centro', 'leste' : 'info leste', 'sul' : 'info sul'}

transito_sp = {}

#loop para carregar as informações de cada região para preparar o retorno
for regiao_atual in regioes_cidade:
    
    regiao = box_dados.find(class_ = regioes_cidade[regiao_atual])
    transito_sp[regiao.find('h3').text.lower()] = regiao.find('h4').text.lower()
 
#retorna um json no terminal com a quantidade de transito na cidade de São Paulo
print(json.dumps(transito_sp, indent=4, ensure_ascii=False))