def arithmetic_arranger(problemas, val=False):
    
    #Creamos una cadena vacia donde estara la solución
    problemas_resueltos = ''
    
    #Primer condicionante de que no debe de haber mas de 5 problemas
    if len(problemas) > 5:
        problemas_resueltos = "Error: Too many problems."
        return problemas_resueltos

    #Obtenemos las operaciones a realizar en una lista 
    operaciones = list(map(lambda x: x.split()[1], problemas))
    #Revisamos el conjunto de operadores aritmeticos si existe uno diferende de + o - retornara un error
    if set(operaciones) != {'+', '-'} and len(set(operaciones)) != 2:
        problemas_resueltos = "Error: Operator must be '+' or '-'."
        return problemas_resueltos

    #Obtenemos los numeros a operar en una lista esta sera de cadenas
    numeros = [] 
    for i in problemas:
        p = i.split()
        numeros.extend([p[0], p[2]])

    #Revisamos que la lista solamente contenga numeros y no asi cadenas
    if not all(map(lambda x: x.isdigit(), numeros)):
        problemas_resueltos = "Error: Numbers must only contain digits."
        return problemas_resueltos

    #Revisamos que los numeros no excedan de 4 digitos
    if not all(map(lambda x: len(x) < 5, numeros)):
        problemas_resueltos = "Error: Numbers cannot be more than four digits."
        return problemas_resueltos


    fila_superios = ''
    dashes = ''
    valores = list(map(lambda x: eval(x), problemas))
    solucion = ''
    for i in range(0, len(numeros), 2):
        space_width = max(len(numeros[i]), len(numeros[i+1])) + 2
        fila_superios += numeros[i].rjust(space_width)
        dashes += '-' * space_width
        solucion += str(valores[i // 2]).rjust(space_width)
        if i != len(numeros) - 2:
            fila_superios += ' ' * 4
            dashes += ' ' * 4
            solucion += ' ' * 4

    fila_inferior = ''
    for i in range(1, len(numeros), 2):
        space_width = max(len(numeros[i - 1]), len(numeros[i])) + 1
        fila_inferior += operaciones[i // 2]
        fila_inferior += numeros[i].rjust(space_width)
        if i != len(numeros) - 1:
            fila_inferior += ' ' * 4

    if val:
        problemas_resueltos = '\n'.join((fila_superios, fila_inferior, dashes, solucion))
    else:
        problemas_resueltos = '\n'.join((fila_superios, fila_inferior, dashes))
    return problemas_resueltos
