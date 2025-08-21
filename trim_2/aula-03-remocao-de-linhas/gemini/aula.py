from dataset import data_set

# Use o caminho correto para o arquivo CSV
FNAME = '../../datasets/adult.csv' 

if __name__ == '__main__':
    data_dict = data_set(FNAME)
    
    print("\n--- Resultados Finais ---")
    print("DataFrame (sem a coluna de classes):")
    print(data_dict['dados'].head()) # Usando .head() para não imprimir o DataFrame inteiro
    print("\nLista de Classes:")
    print(data_dict['classes'][:10]) # Imprime apenas os 10 primeiros elementos
    
    print("\n--- Informações Finais ---")
    for key, value in data_dict.items():
        if key != 'dados' and key != 'classes':
            print(f"{key}: {value}")