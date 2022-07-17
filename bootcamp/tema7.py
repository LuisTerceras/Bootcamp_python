import time

# Ejercicio 1
def Calculadora(a,b):
    text = f"1. Suma\n2. Resta\n3. Multiplicacion\n4. Division"
    opcion = int(input(text + "\n"))
    match opcion:
        case 1:
            print(a+b)
        case 2: 
            print(a-b)
        case 3:
            print(a*b)
        case 4: 
            print(a/b)
        case _:
            print("Error")

Calculadora(5, 5)

# Ejercicio 2
def IrCasa():
    hora = time.strftime("%H:%M:%S",time.localtime())
    lista = hora.split(":")
    horas = int(lista[0])
    min = int(lista[1])
    seg = int(lista[2])
    if hora >= "07:00:00" and hora <= "15:00:00":
        print("Estas en horario de trabajo")
        rh = 15 - horas - 1
        rm = 59 - min
        rs = 59 - seg
        restante = f"{rh}:{rm}:{rs}"
        print(f"En {restante} te vas a casa")
    if hora <= "07:00:00" or hora >= "15:00:00":
        print("Tiempo libre")
   
IrCasa()