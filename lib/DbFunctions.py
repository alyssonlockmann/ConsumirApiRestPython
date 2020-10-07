
import pymongo

class DbFunctions():
    
    # Atributos declarados de forma privada, pois devem ser utilizados apenas dentro da classe.
    __URLDB = '192.168.99.100:27017'
    __USER = 'pythonUser'
    __PASS = 'pythonPass'
    __DATABASE = 'pythonDb'

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
        except Exception as inst:
            print('*** Erro ao inserir lote de registros! Coll: ' + collection)
            print(type(inst))
            print(inst.args[0])