nombre =input("Escribe tu nombre: ")
jose= "me llamo"
c1=int(input("Escribe tu calificacion del Examen 1: "))
c2=int(input("Escribe tu calificacion del Examen 2: "))
c3=int(input("Escribe tu calificacion del Examen 3: "))

t1 = (c1*15)/100
t2 = (c1*20)/100
t3 = (c1*25)/100

Total = c1+c2+c3
faltan = 36- Total
print(nombre, "Alcanzaste ",Total, " puntos, y te faltaron", faltan)