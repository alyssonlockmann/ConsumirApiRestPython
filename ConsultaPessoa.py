#
# Consulta a API e insere o registro no mongoDB
#
import requests
import json
import pymongo
from lib import ApiError
from lib import DbCredentials as db

# Requisição
resp = requests.get('https://randomuser.me/api/')

# Testa pra ver se a requisição deu ok.
# Se deu erro, apresenta a exceção.
if resp.status_code != 200:
    raise ApiError.ApiError(' {}'.format(resp.status_code))

# Pega o request e transforma em json
# A saída do mesmo é um dicionário.
jsonIni = resp.json()

# Formatando e exibindo resumo dos dados que serã inseridos na base.
jsonResults = jsonIni['results']
userDictPrint = 'Nome: {} {} \nFone: {} \nNascimento: {} \nE-mail: {}'.format(jsonResults[0]['name']['first'], jsonResults[0]['name']['last'], jsonResults[0]['phone'], jsonResults[0]['registered']['date'], jsonResults[0]['email'])
print(userDictPrint)

# Configurando conexão com mongoDB e montando inserção na base.
userData = {'nome' : jsonResults[0]['name']['first'] + ' ' + jsonResults[0]['name']['last'], 
            'fone' : jsonResults[0]['phone'],
            'idade': jsonResults[0]['registered']['age'],
            'email': jsonResults[0]['email'],
            'pais': jsonResults[0]['location']['country']
        }

# Inserindo o registro na base. Se deu erro, apresenta a exceção tratada.
db.DbCredentials.mongoInsertOne('pessoas', userData)