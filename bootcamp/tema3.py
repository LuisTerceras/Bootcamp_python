# Ejercicio 1
nombre = "Luis"
apellidos = "Terceras Clayton"
edad = 19
email = "luisproman02@gmail.com"
tel = "+34 638612250"
casado = False
hijos = False
amigos = ["Ismael", "Ruben", "Jout", "Dani"]
peliculas_vistas = {
    "1" : "Gran Torino",
    "2" : "Forest Gump",
    "3" : "Gladiador", 
    "4" : "Ciudadano ejemplar",
    "5" : "Los increibles"
}
print(f"Nombre: {nombre} {apellidos}\nEdad: {edad}\nEmail: {email}")
print(f"Telefono: {tel}\nCasado: {casado}\nHijos: {hijos}\nAmigos: {amigos}")
print(f"Peliculas: {peliculas_vistas}")

# Ejercicio 2
peso = float(input("Introduce tu peso en kilogramos: "))
estatura = float(input("Introduce tu estatura en metros: "))
imc = peso/pow(estatura, 2)
print(f"Tu indice de masa corporal es {round(imc, 2)}")