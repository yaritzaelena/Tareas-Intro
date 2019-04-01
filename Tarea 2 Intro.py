## Problema 1
def formar_lista (num):
    if type (num)== int and num>0:
        return formarlista_aux (num)
    else: return 'Error'

def formarlista_aux (num):
    if num == 0:
        return []
    elif (num%10)%2 == 0:
        return formarlista_aux (num//10)+[num%10]
    else: return formar_lista(num//10)
## Problema 2
def cadena(palabra):
    if type (palabra) == str:
        return cadena_aux (palabra, 0)
    else: return 'Error'

def cadena_aux (palabra, digito):
    if palabra == '':
        return 0
    elif (palabra [0] == 'a' or palabra[0] == 'e' or palabra[0] == 'i'
          or palabra[0] == 'o' or palabra [0] == 'u'):
        return cadena_aux (palabra [1:], digito)
    else: return (digito+1) + cadena_aux (palabra [1:], digito)
## Problema 3
def palindromo (cadena):
    if type (cadena) == str and num > 0:
        return palin (str (num))
    else:return 'Error'
    
def palin (cadena):
    if cadena == '' or len(cadena)==1:
        return True
    elif cadena [0] == cadena [-1]:
        return palin (cadena [1:-1])
    else: return False 
## Problema 4
def intercambiar (lista):
    if type (lista) == list and (len(lista)%2)== 0:
        return intercambiar_aux (lista)
    else: return 'Error'

def intercambiar_aux (lista):
    if lista == []:
        return []
    else: return [lista [1]] + [lista [0]]+ intercambiar_aux (lista [2:])
