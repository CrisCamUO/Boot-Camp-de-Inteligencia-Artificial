#Tipo compuesto
#Lista: recibe elementos que pueden ser de cualquier tipo
lista = ["Cristhian","Unas","ig: cris.tacho0",True,1.63]
  #Cada elemento se encunetra en una posición, se empieza a contar desde 0
print(lista[0],lista[2])
  #Asignar valores a la lista, mediante la posisción
lista[0]="Cris"
print(lista[0])
#Tupla es un tipo de Lista que no se puede modificar
tupla = ("Jugo de Guayaba","Arepa","Huevos revueltos",8.30,True)
print(tupla[2])
print("Yo desayuné: ", tupla[0]," ",tupla[1]," ",tupla[2]," a las ", tupla[3])
  #No se puede asignar valores nuevos a la tupla, pero si a la lista
#tupla(1)="Pan tajado"
#tupla(4)=False
#Creando un conjunto - set {}
conjunto = {"Cristhian","Unas","ig: cris.tacho0",True,1.63}
print(conjunto)
  #No se permiten elementos repetidos en los conjuntos
conjunto2 = {"Cristhian","Unas","ig: cris.tacho0",True,1.63,"Cristhian"}
print(conjunto2)

#Creando un Diccionario {}: Le da un numbre para acceder al elemento
diccionario ={
  "nombre" : "Cristhian",
  "apellido" : "Unas",
  "estatura" : 1.63,
  "Happy" : True,
  #"nombre" : "Cristhian" - Valores repetidos, no aparecen en el print, sólo el original
}
print(diccionario)
print(diccionario["nombre"])
print(diccionario["apellido"])
print(diccionario["estatura"])
print(diccionario["Happy"])
print(diccionario["estatura"]+3)