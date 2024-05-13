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

#session.execute("CREATE TABLE IF NOT EXISTS sensor (id BIGINT, ano INT, mes INT, dia INT, hora INT, leitura FLOAT, PRIMARY KEY ((id, ano, mes), dia, hora));")

#session.execute("ALTER TABLE sensor ADD local TEXT;")
#session.execute("ALTER TABLE sensor ADD modelo TEXT;")











