def conta(lista):
    result = [0,0,0]
    for id in lista:
        idx = id-1
        result[idx] += 1
    print('resultado ==>',result)

def conta_dic(lista):
    result = {'1':0,'2':0,'3':0}
    for item in lista:
        result[item] = result[item] + 1
    print('resultado ==> ',result)

def conta_filtro(lista):
    result = [0,0,0]
    for id in lista:
        if id not in (1,2,3): continue
        idx = id-1
        result[idx] += 1
    print('resultado ==>',result)

def conta_filtro_dict(lista):
    result = {1:0,2:0,3:0}
    for item in lista:
        if item not in (1,2,3): continue
        result[item] = result[item] + 1
    print('resultado ==>',result)

conta([1,2,3,2,1,3,1,1,2])
conta_dic([1,2,3,2,1,3,1,1,2])

conta_filtro([1,2,3,5,4,3,2,5,1,2,3,2,1,1,2,2,2,'banana','maça',1,'banana'])
conta_filtro_dict([1,2,3,5,4,3,2,5,1,2,3,2,1,1,2,2,2,'banana','maça',1,'banana'])