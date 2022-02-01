#strings (cadenas)

# las cadenas son de caracteres, si las sumas las concatena (une) SIN añadir un espacio entre medias
str1 = "Hello "
str2 = "World"
str3 = str1 + str2
print (str3)

#las cadenas al ser letras hace falta transformarlas en números si quieres trabajar con una string de numeros
str1 = 123
str2 = int(str1) + 1
print (str2)

#input recoge una cadena (string) por lo que para realizar operaciones numericas debes transformarla a numeros con int() float()
str1 = int(input ("Dime un número: "))
str2 = str1 + 10
print (str2)
print ('\n')

# cadena[algo] algo marca a que altura de la cadena quieres hacer algo, empezando desde el 0.
fruit = "banana"
print (fruit[3])
print (fruit[0])

# len ()  proviene de length, lo que nos marca la longitud de la cadena, por tanto len(casa) = 4; len (banana) = 6
print (len (fruit))
print ('\n')

fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print (index, letter)
    index += 1


count = 0
for letter in fruit:
    print(letter)
    if letter == "a":
        count += 1

print ("hay", count, "A's en esta palabra")



#Puedes utilizar posiciones dentro de las cadenas:

fruits = "Banana and Apple"

print (fruits[3:16])
print (fruits[:5])
print (fruits[:])

fruit = 'apple'
boolean = 'x' in fruit
print (boolean)
if 'ppl' in fruit:
    print ('Encontrado!!')