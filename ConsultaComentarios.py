#
# Consulta a API, salva os dados em um 
#
import requests
import json
import pymongo
from lib import ApiError
from lib import DbCredentials as db
import pandas as pd

mongoCrdtls = db.DbCredentials()
print(mongoCrdtls.DATABASE)

# Caminho do arquivo
PATH = 'Arquivos/input'

# Requisição
resp = requests.get('http://jsonplaceholder.typicode.com/comments')

# Testa pra ver se a requisição deu ok.
# Se deu erro, apresenta a exceção.
if resp.status_code != 200:
    raise ApiError.ApiError(resp.status_code)

# Pega o request e transforma em json
# A saída do mesmo é uma lista.
jsonIni = resp.json()
jsonString = json.dumps(jsonIni)

# Veriifica se o arquivo foi carregado corretamente.
try:
    df = pd.read_json(jsonString)
except Exception as inst:
    print('*** Erro ao carregar dados de entrada!')
    raise inst

# Cria df de comentários. 
dfCmts = df.drop(['id', 'name', 'email'], axis=1)
print(dfCmts)

# Retira a coluna body do df. 
df.drop('body', axis=1, inplace=True)
print(df)


