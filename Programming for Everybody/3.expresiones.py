#constantes
#para decimales el punto, la coma diferencia variables. El print de letras se puede hacer con 'asd'  o "asd"


print (98.3)
print (98,3)
print ('Hello world'); print ("Hello world v2.0")

#variables -> la ultima sobrescribe a la anterior
#variable name rules
#debe empezar con una letra o una _       #y no se puede usar otra cosa que no sean letras, numeros o _   ej: prohibido usar .
#considera diferentes variables con mayus y sin, ej: spam =/ SPAM =/ Spam

spam = 12.2
SPAM = 14
spam = 100
print (spam,SPAM, '\n')

a = 5
b = 3.3
c = a * b
d = 17

print (d/a)
print (d//a)
print (int(d/a))
print (c, '\n')  

#expresiones numéricas raras ( ** que significa elevado, y % que significa resto de una division)
print (4 ** 3)
print (23 % 5)

#puedes sumar palabras para realizar una frase
aaa = 'hello ' + 'there'
print (aaa)

#input para recoger strings.    La coma en el print hace un espacio y es para añadir variables despues de la coma
nam = input ('Whats your name?\n')
print ('hello', nam, '\n\n\n')

inp = input('Europe floor? ')
USf = int(inp) + 1
print ('US floor:', USf)

#Eres un caraculo
