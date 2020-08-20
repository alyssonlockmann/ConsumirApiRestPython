
import pymongo

class DbCredentials():
        
    URLDB = '192.168.99.100:27017'
    USER = 'pythonUser'
    PASS = 'pythonPass'
    DATABASE = 'pythonDb'
    
    @classmethod
    def mongoInsertOne(self, collection, data):
        mongoClient = pymongo.MongoClient('mongodb://' + self.USER + ':' + self.PASS + '@' + self.URLDB + '/' + self.DATABASE)
        database = mongoClient[self.DATABASE]
        coll = database[collection]

        try:
            coll.insert_one(data)
            print('Registro inserido com successo!')
        except Exception as inst:
            print('*** Erro ao inserir registro: ')
            print(type(inst))
            print(inst.args[0])

    