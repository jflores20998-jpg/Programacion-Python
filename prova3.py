def canvi(x):
    x = x+1
    print(x)
def canvireferencia(llista):
    if len(llista) >0:
        llista[0] ="Guapo"
    else:
        print("No te cap valor")
#programa principal
global marc = 3 
nombre=3
canvi(nombre)
print(nombre)
real = 3.12141516
bool = False
cadena = "hola, ramis!"
print (cadena)
llista = [3, [4, 5], (1, 2, 3), "hola"]
canvireferencia(llista)
print(llista[0])
tupla = (1, 3, 3, 4,)
rag = range(1, 11, 2)
diccionari = {"nom":"Jair", "cognom":"Ramis", "edat": 28, "telefon": 123456789}
nombre = 4
llista[3] = "hola, mon!"
print(llista[3])
marc = 