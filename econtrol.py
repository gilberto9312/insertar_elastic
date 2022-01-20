#from faker import Factory
from datetime import datetime
from elasticsearch import Elasticsearch
import json
import datetime
# esDomainEndpoint = "http://localhost:9200"
# es = Elasticsearch(esDomainEndpoint)
# es = Elasticsearch(
#    ['url'],
#    http_auth=('usuario', 'password'),
#    scheme="https",
#    port=443,
#)

def create_names():
    for x in range(250000):

        print("--------------------------------------------------------------------")
        print(datetime.datetime.now().timestamp())
        print(x)
        #genUname = fake.slug()
        #genName = fake.name()
        #genText = fake.text()
        #catalogoId = fake.random_int(min=100000000000, max=9999999999999)
        #description = fake.text()
        #idFake = fake.random_int(min=100000000000, max=9999999999999)
        go = es.index(
            index="transacciones_rest",
            #doc_type="transacciones_rest",
            id=datetime.datetime.now().timestamp(),
            body={
                  "id" : datetime.datetime.now().timestamp(),
                  "id_factura" : datetime.datetime.now().timestamp(),
                  "extras" : {
                    
                  },
                  "metodoconfirmacion" : "POST",
                  "filtros" : [
                  ],
                  "registro_id" : datetime.datetime.now().timestamp(),
                  "registro_fecha_creacion" : 1642526191,
                  "registro_fecha_actualizacion" : 1642526191,
                  "registro_fecha_gestion" : 1642538855,
                  "registro_puntaje" : 100,
                  "registro_reglas_activadas" : 1,
                  "registro_verificado" : 'false',
                  "registro_id_estado_econtrol" : 2,
                  "registro_id_estado_gestion" : 0,
                  "registro_estado_econtrol" : "Denegada",
                  "registro_estado_gestion" : 'null'
                }
        )
        
       # print(json.dumps(idFake))
if __name__ == '__main__':
    #fake = Factory.create()
    create_names()
