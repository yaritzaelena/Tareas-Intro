## Problema 1
def multiplicacion (lista):
    if type (lista)==list:
        return multiplicacion_aux (lista, 0)
    else: return 'Error'

def multiiplicacion_aux (lista, 0):
    if lista == []:
        return []
    if lista [0] >= 0:
        return [lista[0]*i] + multiplicacion_aux (lista [1:], i+1)
## Problema 2
def suma (listax):
    if type (listax) == list:
        return suma_aux (listax, 1)
    else: return 'Error'

def suma_aux (lista, exponente):
    if lista == []:
        return 0
    if type (lista) == list:
        return suma (lista [0]+lista [1:])
    if lista [0] >=0:
        return lista [0] ** exponente + suma_aux (lista [1:], exponente+1)
## Problema 3
def summ(num):
    if type (num)== int:
        return summ_aux(num, 3*1-1, 1, 1)
    else: return 'Error'
def summ_aux (num, constante, n, d):
    if d == num:
        return 0
    else: return (constante + (constante*3*n-d)) + summ_aux (num, constante, (n+1)**2, d+1)
## Problema 4
def intercambiar (numero):
    if type (numero) == int:
        return intercambiar_aux (numero, 1)
    else: return 'Error'
def intercambiar_aux (numero, potencia):
    if numero == 0:
        return 0
    if (numero%10)>0:
        return (((numero%10)*(10**potencia)+((numero//10)%10)*(10**(potencia-1)))
                + intercambiar_aux (numero//100, potencia+1))


