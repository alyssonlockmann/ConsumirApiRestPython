#
# Consulta a base mongoDB e retorna os dados para o período e collection  informadas.
# Os parametros devem ser strings e estar ordenados
#
from lib import DbFunctions as db
import pandas as pd
import sys

if len(sys.argv) -1 < 3:
    print('Parametros de entrada obrigatórios para execução do script!')
    print('Os mesmo devem serguir a ordem: NOME_COLLECTION, DATA_INICIAL, DATA_FINAL')
    print('Exemplo: python ConsultaPeriodoColl.py nome_collection 01-01-2021 01-02-2021')
else:
    try: 
        coll = sys.argv[1]
        data_ini = sys.argv[2]
        data_final = sys.argv[3]

        # Consultando registros na collection 'comentarios'.
        findResult = db.DbFunctions.mongo_find_interval(coll, data_ini, data_final)

        listResult = pd.DataFrame(findResult)
        listIndex = listResult.index

        # Apresentando resultado:
        print('Registros encontrados:')
        print(len(listIndex))
        print(listResult.head())

    except Exception as inst:
        print('Erro ao executar consulta dos dados!')
        print(type(inst))
        print(inst.args[0])



