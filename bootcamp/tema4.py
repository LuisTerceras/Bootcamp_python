# Ejercicio 1
edad = int(input("Que edad tienes?\n"))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Ejercicio 2

numero_inicial = int(input("Introduce el numero inicial del rango\n"))
numero_final = int(input("Introduce el numero final del rango\n"))
contador = numero_inicial
rango_numeros = []
impares = []

while contador <= numero_final:
    rango_numeros.append(contador)
    contador+=1

for impar in rango_numeros:
    if impar % 2 == 1:
        impares.append(impar)

 
print(impares)

# Ejercicio 3
contador = 100
while contador > 0:
    print(contador, end=" ")
    contador-=1