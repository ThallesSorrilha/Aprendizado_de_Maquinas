import numpy as np
# 12- fazer o transpose da tabela e armazenar em outra variável: tabela_t
#       imprimir a tabela normal e sua transposta
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z', '@', '#', '*', '+']
print(lista)
lista = np.array(lista)     
lista = lista.reshape(-1,10)
print(lista)
lista_t = lista.T  
print(lista_t)

# 14- transformar a tabela em um shape (10, 3), armazenar em tabela2. 
#       Imprimir cada linha da tabela2
#       Comparar o resultado com a pergunta: 
tabela2 = lista.reshape(10, 3)
for linha in tabela2:
    print('linha---->',linha)
    
    
# 15- imprimir as colunas da tabela2
for coluna in tabela2.T:
    print('coluna -->',coluna)
    
#16- capturar da tabela, os elementos do meio, e colocar na variável: tabela3
#       Imprimir a tabela3. Abaixo o que deve aparecer:
#       ['h' 'i' 'j' 'k']
#       ['n' 'o' 'p' 'q']
#       ['t' 'u' 'v' 'w']

tabela3 = lista[1:-1][1:-1]

# -1 -> quando não se sabe a dimensão correta da linha ou coluna
tabela5 = lista.reshape(-1, 5)
print(tabela5)

print('shape -->', tabela3.shape)
print('shape -->', tabela5.shape)

lista3 = tabela3.toList()
lista5 = tabela5.toList()
print(lista3)
print(lista5)

lista3 = tabela3.flatten()
lista5 = tabela3.flatten()
print(lista3)
print(lista5)

# tarefa
lista3 = [item for sublist in lista3 for item in sublist]