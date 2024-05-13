from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

import json

auth = {}

with open('dbiot-token.json') as f:
    auth = json.load(f)

cloud_config = {
    'secure_connect_bundle': 'secure-connect-dbiot.zip'
}
auth_provider = PlainTextAuthProvider(
    username=auth['clientId'], 
    password=auth['secret']
)

cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")

session.set_keyspace('ksiot')


carro_fornecido = input("Digite o modelo do carro para consultar o estoque: ")

query = f"SELECT nome, estante, quantidade FROM estoque WHERE carro = '{carro_fornecido}'"
result = session.execute(query)
for row in result:
    print(f"Nome: {row.nome}, Estante: {row.estante}, Quantidade: {row.quantidade}")











