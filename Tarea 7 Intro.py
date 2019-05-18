class Sumatoria(object):
    def __init__(self):
        pass
    def sumatoria (self, matriz):
        if type (matriz) == list and (len(matriz)== len (matriz[0])):
            return self.sumaColumna(matriz, 0, 0, 0), self.sumaFila(matriz, 0,0,0), self.antidiagonal(matriz, (len(matriz)-1), 0)
        else: return 'Error'

    def sumaColumna(self, matriz, f, c, r):
        if f == len(matriz):
            return r
        if c == len(matriz[0]):
            return self.sumatoria (matriz, f+1, 0, r)
        if c == matriz[f][0]:
            return self.sumatoria (matriz, f, c+1, r+ m[f][c])
        if c == len(matriz[0])-1:
            return self.sumatoria (matriz, f, c+1, r+ m[f][c])

    def sumaFila (self, matriz, f, c, r):
        if f == len(matriz):
            return r 
        if c == len (matriz[0]):
            return self.sumaFila(matriz, f+1, 0, r+ m[f][c])
        else: return self.sumaFila (matriz, 0, c+1, r+ [f][c])

    def antidiagonal(self, matriz, indice, r):
        if indicee == -1:
            return result
        else: return self.antidiagonal(m1, indice-1, result + matriz[indice][-(indice+1)])


class Estdistica (object):
    def __init__ (self, matriz):
        pass
                                                                                                      
    def estadistica (self, matriz):
        if type (matriz) == list:
            return self.diagonal (0, 0, matriz, 1), self.mediana(matriz, ((len(matriz)+1)/2), ((len(matriz)/2)+1))
        else: return 'Error'
    def diagonal(self, indice, resultado, matriz, indice2):
        if indice == len (matriz):
            return resultado/indice2
        else: return self.diagonal_aux(indice+1, resultado + matriz[indice][indice], matriz, indice2+1)
                                                              
    def mediana(self, matriz, i_1, i_2):
        if len (matriz)%2 == 1:
           return i_1
        if len (matriz)%2 == 2:                                                                                              
           return (i_1+i_2)/2                                 
class Polinomio (object):
     def __init__ (self):                                                                                                 
         pass                           
     def polinomio (self, num1, num2):
        if type (num1) == int and type (num2)== int  and num1<= 50:
             return self.polinomio_aux (num1, num2, 1, 1)
        else: return 'Error'
     def polinomio_aux (self, num1, num2, r, s):
         
        if ((-r)+ (-s)) == num1 and ((-r)+(-s))== num2:
             return (-r, -s)
        if ((-r)+ (s)) == num1 and ((-r)+(s))== num2:
            return (-r, s)
        if ((r)+ (-s)) == num1 and ((r)+(-s))== num2:
             return (r, -s)        
        if s <= 49:
            return self.polinomio_aux (num1, num2, r+1, 1)
        else: return self.polinomio_aux (num1, num2, r, s+1)

class Notacion (object):
    def __init__ (self):
        pass
    def notacion (self, num):
        return self.notacion_aux(num,0, 0)
    def notacion_aux (self, num, i, a):
        if 1 <= num and num < 10 and num == int:
            return (a*10**i)
        elif num > 0:
            return self.notacion_aux (num//10, i+1)
        else: 
            return self.notacion_aux (num*10, i-1)
    

             


             
