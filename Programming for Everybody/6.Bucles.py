#FOR se utiliza para bucles de X veces o entre 2 puntos 

#for "algo" in range (X) hace una cuenta de 0 hasta X-1 ya que entra al búcle X veces.
'''
for x in range (4):
    print (x)
print ("\n")

for x in range (2,6):
    print (x)
print ("\n")

friends = ["Hector", "Carlos", "Estefania", "Monica", "Jorge"]
for friend in friends:
    print (friend)

print ("\nDone")

for i in [2,4,5,6,3]:
    print (i)

#break sirve para romper los bucles cuando quieras
for z in range (10,20):
    print (z)
    if z >= 15:
        break
print ("\n")

''' 
# Encambio WHILE se utiliza para iterar infinitas veces hasta una condición concreta impuesta en el while
'''
n = 5
while n >= 0:
    print (n)
    n -= 1
    
print ("Escribe 'done' cuando quieras acabar el loop")
while True:
    x = raw_input ("> ")
    if x == "Done":
        break
    elif x == "done":
        break
    elif x[0] == "#":
        continue

    print (x)

print ("El bucle ha terminado")

''' 
#CONTINUE vuelve al inicio del loop,  #BREAK sale del loop directamente   
#RETURN devuelve un valor cuando el loop espera devolver algo y termina el loop

# ejercicio de bucles: buscame el número mas largo

nMayor = -1
print ("Añade 6 números y te diré cual es el mayor de ellos: ")
a = input ("1º:")
b = input ("2º:")
c = input ("3º:")
d = input ("4º:")
e = input ("5º:")
f = input ("6º:")

for numero in [a, b, c, d, e, f]:
    if int(numero) > int(nMayor):
        nMayor = numero

print ("El mayor de los 6 números es:", nMayor)

#Boolean Varible -->  True or False
found = False
for value in [a,b,c,d,e,f]:
    if value == "3":
        found = True
        break
print ("El número 3 ha sido encontrado entre los numeros de muestra?", found)

# none = ninguno, sin valor existente
smallest = None
for value in [a,b,c,d,e,f]:
    if smallest is None:
        smallest = (value)
    elif int (value) < int (smallest):
        smallest = value
    print (smallest, value)
print ("El número menor es: ", smallest)


# is devuelve True si ambos marcan el mismo objeto. == devuelve True cuando las dos variables son iguales

a = [1,2,3]
b = a[:]

print (b == a)
print (b is a)

