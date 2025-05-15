import json
# falta saber como se importa um arquivo .json

lista = [1,2,3,3,2,1,1,1,2]
lista2 = ["mar", "maça", "banana", "mar"]

def baixar_json(_arquivo):
    with open(_arquivo, 'r') as interno:
        return json.load(interno)
    
def contar(_lis):
    resp = {}
    for item in _lis:
        if item not in resp:
            resp[item] = 0
        resp[item] += 1
    return resp

arquivo = baixar_json('pessoa.json')
print('result ->', contar(arquivo))
