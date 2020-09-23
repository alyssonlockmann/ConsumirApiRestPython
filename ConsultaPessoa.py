#
# Consulta uma API que retorna um registro json e insere o dado na base mongoDB
#
import requests
import json
from lib import ApiError
from lib import DbFunctions as db

# Requisição
resp = requests.get('https://randomuser.me/api/')

# Testa pra ver se a requisição deu ok.
# Se deu erro, apresenta a exceção.
if resp.status_code != 200:
    raise ApiError.ApiError(resp.status_code)

# Pega o request e transforma em json
# A saída do mesmo é um dicionário.
jsonIni = resp.json()

# Formatando e exibindo resumo dos dados que serão inseridos na base.
jsonResults = jsonIni['results']
userDictPrint = 'Nome: {} {} \nFone: {} \nNascimento: {} \nE-mail: {}'.format(jsonResults[0]['name']['first'], jsonResults[0]['name']['last'], jsonResults[0]['phone'], jsonResults[0]['registered']['date'], jsonResults[0]['email'])
print(userDictPrint)

# Montando dicionario do registro.
userData = {'nome' : jsonResults[0]['name']['first'] + ' ' + jsonResults[0]['name']['last'], 
            'fone' : jsonResults[0]['phone'],
            'idade': jsonResults[0]['registered']['age'],
            'email': jsonResults[0]['email'],
            'pais': jsonResults[0]['location']['country']
        }

# Inserindo o registro na base. Se deu erro, apresenta a exceção tratada.
db.DbFunctions.mongoInsertOne('pessoas', userData)

