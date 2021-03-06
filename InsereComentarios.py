#
# Consulta a API, fatia os dados e posteriormente insere em uma base mongoDB.
#
import requests
import json
from lib import ApiError
from lib import DbFunctions as db
import pandas as pd
from datetime import datetime,timedelta
from jproperties import Properties

# Lendo arquivo de propriedades
configs = Properties()

with open('config/app-config.properties', 'rb') as config_file:
        configs.load(config_file)

# Requisição
resp = requests.get(configs.get('URL_COMENTARIOS').data)

# Testa pra ver se a requisição deu ok.
# Se deu erro, apresenta a exceção.
if resp.status_code != 200:
    raise ApiError.ApiError(resp.status_code)

# Pega o request e transforma em json
# A saída do mesmo é uma lista.
jsonIni = resp.json()
jsonString = json.dumps(jsonIni)

# Veriifica se os dados foram carregados corretamente.
try:
    df = pd.read_json(jsonString)
except Exception as inst:
    print('*** Erro ao carregar dados de entrada!')
    raise inst

# Adicionado data da consulta.
df['data'] = datetime.now()

# Renomeando coluna id.
df = df.rename(columns={'id': 'id_user'})

# Cria df de comentários e apresenta resultado. 
dfCmts = df.drop(['name', 'email'], axis=1)

# Retira a coluna body do df e apresenta resultado.
df.drop('body', axis=1, inplace=True)

# Transforma os dfs para inserir na base.
dfCmts = dfCmts.to_dict('records')
df = df.to_dict('records')

# Inserindo registros na base.
db.DbFunctions.mongo_insert_many('comentarios', dfCmts)
db.DbFunctions.mongo_insert_many('posts', df)
  