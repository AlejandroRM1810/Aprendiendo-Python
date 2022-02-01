#Funciones
def thing ():
    print ('Hello')
    print ('World')

print ('Zip')
thing ()

#el max y min trabaja en ASCII por tanto:   letras minisculas > letras Mayusculas > espacio   ,por lo que la letra mayor será la w al ser la minuscula que mas al final esta del alfabeto y la menor el espacio
big = max('Hello world')
print (big)
tiny = min('Hello world')
print (tiny)

#max no reconoce numeros compuestos como el 14 o 24 por lo que según el código ASCII el mayor será el 8, el menor será de nuevo el espacio
big = max('1 3 5 7 14 24 8')
print (big)
tiny = min('1 3 5 7 14 24 8')
print (tiny)

## funcion con parametro de entrada que te saluda en función de tu idioma, transforma cualquier respuesta a minuscula para despues comparar
def saludar(ey):
    if ey == 'es':
        return 'Hola'
    elif ey == "fr":
        return "Bonjour"
    elif ey == "en":
        return "Hello"
    else:
        return "No esta dentro de los idiomas existentes en el programa"
name = input ('Dime tu nombre: ')
ey = input ('En que idioma te saludo (es,fr,en): ')
ey=ey.lower()
print (saludar(ey), name)

def sumar (a, b):
    suma = (a) + (b)
    return suma

a = float (input ('Dime un número: '))
b = float (input ("Dime otro numero: "))
print ('La suma de los dos números anteriores es', sumar(a,b),'\n')

