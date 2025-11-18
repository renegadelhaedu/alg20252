#importar pacote com funcoes - instalei requests
import requests

pag = requests.request('GET', ' https://infosacc.com.br')
print(pag.text)

