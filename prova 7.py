l=list()
for i in range(5):
    l.append(int(input("intro un numero: ")))
l2=list()
for i in range (4, -1, -1):
    l2.append(l[i])
print(l2)

#Sumar tots els elements de la llista
#suma=0
#for e i in l:
#   suma = suma + e
#print("La suma dels elements de la llista és: {}".format(suma))

# A cada element de la llista sumar un numero llegit per taclat
#num =int(input("intro el numero a sumar: "))
#for i in range(len(l)):
#   l[i] = l[i] + num
#for e in l:
#   print(e)    