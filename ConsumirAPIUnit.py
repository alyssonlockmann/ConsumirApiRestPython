import requests
import json
import pymongo
from lib import ApiError

# Dados de acesso a base de dados.
URLDB = '192.168.99.100:27017'
USER = 'pythonUser'
PASS = 'pythonPass'
DB = 'pythonDb'

# Requisição
resp = requests.get('https://randomuser.me/api/')

# Testa pra ver se a requisição deu ok.
# Se deu erro, apresenta a exceção.
if resp.status_code != 200:
    raise ApiError.ApiError(' {}'.format(resp.status_code))

# Pega o request e transforma em json
# A saída do mesmo é um dicionário.
jsonIni = resp.json()

jsonResults = jsonIni['results']
userDictPrint = 'Nome: {} {} \nFone: {} \nNascimento: {} \nE-mail: {}'.format(jsonResults[0]['name']['first'], jsonResults[0]['name']['last'], jsonResults[0]['phone'], jsonResults[0]['registered']['date'], jsonResults[0]['email'])
print(userDictPrint)

# Configurando conexão com mongoDB e montando inserção na base.
mongoClient = pymongo.MongoClient('mongodb://' + USER + ':' + PASS + '@' + URLDB + '/' + DB)
database = mongoClient['pythonDb']
coll = database['pessoas']
userData = {'nome' : jsonResults[0]['name']['first'] + ' ' + jsonResults[0]['name']['last'], 
            'fone' : jsonResults[0]['phone'],
            'Nascimento': jsonResults[0]['registered']['date'],
            'email': jsonResults[0]['email']
        }

# Inserindo o registro na base. Se deu erro, apresenta a exceção tratada.
try:
    coll.insert_one(userData)
    print('Registro inserido com successo!')
except Exception as inst:
    print('*** Erro ao inserir registro: ')
    print(type(inst))
    print(inst.args[0])
    


#Ler todos os registros do elemento df
#for x in resultInsert:
#  print(x)
