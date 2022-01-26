#Funciones
def thing ():
    print ('Hello')
    print ('World')

print ('Zip')
thing ()

##

big = max('1 3 5 7 14 24 8')
print (big)
tiny = min('1 3 5 7 14 24 8')
print (tiny)

## funcion con parametro de entrada
def saludar(ey):
    if ey == ("es" or "Es" or "ES"):
        return "Hola"
    elif ey == "fr":
        return "Bonjour"
    elif ey == "en":
        return "Hello"
    else:
        print ("No esta dentro de los idiomas existentes en el programa")
        return " "
name = input ('Dime tu nombre: ')
ey = input ('En que idioma te saludo (es,fr,en): ')
print (saludar(ey), name)

def sumar (a, b):
    suma = (a) + (b)
    return suma
9
a = float (input ('Dime un número: '))
b = float (input ("Dime otro numero: "))
print ('La suma de los dos números anteriores es', sumar(a,b),'\n')

