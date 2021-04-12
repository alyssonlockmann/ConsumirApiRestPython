
import pymongo
from datetime import datetime, timedelta
from jproperties import Properties

class DbFunctions():
    # Carregando arquivo de propriedades.
    __configs = Properties()

    with open('config/app-config.properties', 'rb') as __config_file:
        __configs.load(__config_file)
    
    # Atributos declarados de forma privada, pois devem ser utilizados apenas dentro da classe.
    __URLDB = __configs.get('URLDB').data
    __USER = __configs.get('USER').data
    __PASS = __configs.get('PASS').data
    __DATABASE = __configs.get('DATABASE').data

    # Criando e configurando o cliente do mongoDB, também privados.
    __mongoClient = pymongo.MongoClient('mongodb://' + __USER + ':' + __PASS + '@' + __URLDB + '/' + __DATABASE)
    __database = __mongoClient[__DATABASE]
    
    @classmethod
    def mongo_insert_one(self, collection, data):
        ''' Insere um registro unico na base. 
        \nO paramêtro "data" recebe um dicionário('dict')'''

        coll = self.__database[collection]

        try:
            coll.insert_one(data)
            print('Registro inserido com successo! Coll: ' + collection)
        except Exception as inst:
            print('*** Erro ao inserir registro! Coll: ' + collection)
            print(type(inst))
            print(inst.args[0])

    @classmethod
    def mongo_insert_many(self, collection, data):
        ''' Insere varios registros na base. 
        \nO paramêtro "data" recebe uma lista('list') '''

        coll = self.__database[collection]

        try:
            coll.insert_many(data)
            print('Lote de registros inserido com successo! Coll: ' + collection)
            print('Registros no lote: {}'.format(len(data)))
        except Exception as inst:
            print('*** Erro ao inserir lote de registros! Coll: ' + collection)
            print(type(inst))
            print(inst.args[0])

    @classmethod
    def mongo_find_interval(self, collection, date_ini, date_final):
        '''Busca dados de um período da collection informada.
        \nOs parâmetros "date_ini" e "date_final" recebe data no formato "dd-mm-yyyy".'''
        coll = self.__database[collection]
        
        date_gte = datetime.strptime(date_ini, '%d-%m-%Y')
        date_lte = datetime.strptime(date_final, '%d-%m-%Y')

        try:
            result = coll.find({ "data": { "$gte": date_gte , "$lte": date_lte}})
            print('Período consultado: ' + date_ini + ' até ' + date_final)
            return result
        except Exception as inst:
            print('*** Erro ao consultar registros! Coll: ' + collection + ' Periodo: ' + date_ini + ' / ' + date_final)
            print(type(inst))
            print(inst.args[0])


        
        
        

