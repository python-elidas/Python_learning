def print_dict_cols(diccionario:dict):
    #imprimiremos un diccionario dándole estructura verticalmente y en columnas 
    for key in diccionario.keys():
        print(f'{key}: {diccionario[key]}')
    
def print_dict_vertical(diccionario:dict):
    for clave, valor in diccionario.items():
        print(f'{clave}:')
        if isinstance(valor, dict):
            print_dict_vertical(valor)
        elif isinstance(valor, (list, tuple, set)):
            for item in valor:
                if isinstance(item, dict):
                    print_dict_vertical(item)
                else:
                    print(f'- {item}')
        else:
            print(f'- {valor}')
    