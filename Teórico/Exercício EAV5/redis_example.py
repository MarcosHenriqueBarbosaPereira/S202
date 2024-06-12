import redis 

redis_conn = redis.Redis(
    host="redis-18230.c263.us-east-1-2.ec2.redns.redis-cloud.com", 
    port=18230,
    username="default", # use your Redis user. More info https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl/
    password="ncUfYRQYYpgc7lU7i9g7snBS7esFFCXI", # use your Redis password
    decode_responses=True
)

# redis_conn.hset("product:2", mapping={
#     "nome": "Macbook",
#     "preco": 12999.99,
#     "marca": "Apple",
#     "descricao": "Um notebbok simples de entrada"
# })

# redis_conn.lpush("estoque", "poduct:1","product:2")

# redis_conn.lrem("estoque", 1,"poduct:1" )
# # redis_conn.lpush("estoque", "product:1")

# tamanho_estoque = redis_conn.llen("estoque")

# estoque = redis_conn.lrange("estoque", 0, tamanho_estoque-1)
# print(estoque)
# for produto in estoque:
#     print(redis_conn.hget(produto, "nome"))
#     print(redis_conn.hget(produto, "preco"))
#     print()

users = [
        {"id":'1', "nome":"Serafim Amarantes", "email":"samarantes@g.com"},
        {"id":'2', "nome":"Tamara Borges", "email":"tam_borges@g.com"},
        {"id":'3', "nome":"Ubiratã Carvalho", "email":"bira@g.com"},
        {"id":'4', "nome":"Valéria Damasco", "email":"valeria_damasco@g.com"}
    ]

interests = [
        {"usuario":1, "interesses": [{"futebol":0.855}, {"pagode":0.765}, {"engraçado":0.732}, {"cerveja":0.622}, {"estética":0.519}]},
        {"usuario":2, "interesses": [{"estética":0.765}, {"jiujitsu":0.921}, {"luta":0.884}, {"academia":0.541}, {"maquiagem":0.658}]},
        {"usuario":3, "interesses": [{"tecnologia":0.999}, {"hardware":0.865}, {"games":0.745}, {"culinária":0.658}, {"servers":0.54}]},
        {"usuario":4, "interesses": [{"neurociências":0.865}, {"comportamento":0.844}, {"skinner":0.854}, {"laboratório":0.354}, {"pesquisa":0.428}]}
    ]
    
def questao_1(users):

    results = []
    
    for user in users:
        redis_conn.hset("user:"+user['id'], mapping={
            "id": user['id'],
            "nome": user['nome'],
            "email": user['email']
        })

        results.append(redis_conn.hgetall("user:"+user['id']))

    return results

#print(questao_1(users))

def questao_2(interests):

    results = []
    
    for interest in interests:
        for i in interest['interesses']:
            redis_conn.lpush("usuario:"+str(interest['usuario']), i)

        results.append(sorted(redis_conn.lrange("usuario:"+str(interest['usuario']), 0, -1)))
        
    return results

print(questao_2(interests))

redis_conn.flushall()