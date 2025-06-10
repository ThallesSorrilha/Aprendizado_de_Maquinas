
texto = "quem com ferro fere com ferro será ferido"

letras = ['a', 'e', 'i', 'o', 'u']

# parametro: str    - anotação que indica o tipo esperado de parâmetro
# -> int            - anotação que indica o tipo esperado de retorno
def soma_vogais(txt: str, let: str) -> int:
    soma_letras = 0
    for char in txt:
        if let.__contains__(char):
            soma_letras += 1
    return soma_letras

soma_vogais(texto, letras)

def manipular_numeros():
    lista_geral = []
    for i in range(10):
        numero = int(input("Digite um número: "))
        if numero == 0:
            break
        lista_geral.append(numero)

    numeros_positivos = []
    numeros_negativos = []
    contador_positivos = 0
    contador_negativos = 0
    for numero in lista_geral:
        if numero < 0:
            numeros_negativos.append(numero)
            contador_negativos += 1
        else:
            numeros_positivos.append(numero)
            contador_positivos += 1

    print("lista geral: ", lista_geral)
    print("lista positivos: ", numeros_positivos)
    print("lista negativos: ", numeros_negativos)
    print("soma de positivos: ", sum(numeros_positivos))
    print("soma de negativos: ", sum(numeros_negativos))
    print("contagem de positivos: ", contador_positivos)
    print("contagem de negativos: ", contador_negativos)
    print("media de negativos: ", sum(numeros_negativos) / len(numeros_negativos))
    print("media de positivos: ", sum(numeros_positivos) / len(numeros_positivos))

manipular_numeros()


def lanchonete():
    cardapio = {}
    cardapio['xbug'] = 7.30

    print(cardapio)