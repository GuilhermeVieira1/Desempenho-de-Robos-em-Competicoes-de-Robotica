def imprimir_objetos(cabecalho, objetos):
    print(f'\n {cabecalho}')
    for indice, objeto in enumerate(objetos):
        formato = '{:<2} {}'
        if indice < 9:
            print(formato.format(f'0{indice+1} - ', str(objeto)))
        else:
            print(formato.format(f'{indice + 1} - ', str(objeto)))