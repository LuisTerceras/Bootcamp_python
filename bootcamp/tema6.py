# Ejercicio 1
class Vehiculo():
    color = ""
    ruedas = 0
    puertas = 0
    
    def __init__(self,color, ruedas, puertas) -> None:
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0
    
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def text(self):
        text = f"Color: {self.color}\nRuedas: {self.ruedas}\nPuertas: {self.puertas}\n"
        text+= f"Velociadad: {self.velocidad}\nCilindrada: {self.cilindrada}"
        return text

c = Coche("Amarillo", 4, 5, 250, 12)
print(c.text())

# Ejercicio 2
class Alumno:
    nombre = ""
    nota = 0
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def text(self):
        if self.nota >= 5:
            return f"Nombre: {self.nombre}\nHas aprobado con un {self.nota}"
        return f"Nombre: {self.nombre}\nHas suspendido con un {self.nota}"
    
a = Alumno("Luis Terceras", 4)
a2 = Alumno("Alvaro Hilero", 6)
print(a.text()+ "\n" + a2.text())