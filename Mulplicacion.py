def multiplicacion (lista):
    if type (lista) == list:
        return multiplicacion_aux (lista, 0)
    else: return 'Error'

def multiplicacion_aux (lista, i):
    if lista == []:
        return []
    if lista [0]>= 0:
        return [lista [0]* i] + multiplicacion_aux (lista [:-1], i+1)
