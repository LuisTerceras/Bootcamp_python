import math

# Ejercicio 1
def AreaTriangulo(base, altura):
    return round(base*altura/2, 2)

def AreaCirculo(radio):
    return round(pow(radio,2)*math.pi,2)

print(AreaTriangulo(13,4))
print(AreaCirculo(5))

# Ejercicio 2
def EsPrimo(n):
    contador = 2
    if n > 2:
        while contador <= n-1:
            if n % contador == 0:
                return False
            contador +=1
    return True

print(EsPrimo(359))

# Ejercicio 3
def EsBisiesto(año):
    if año%4==0 and año%100!=0 or año%400==0:
        return True
    return False

print(EsBisiesto(2100))