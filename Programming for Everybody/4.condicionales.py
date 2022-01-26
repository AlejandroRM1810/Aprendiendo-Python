#Condicionales
x = 5
if x > 10:
    print ('Numero grande')
if x < 10:
    print ('Numero pequeño')
 
print ('Finish\n')

#     < <= == >= > !=

if x == 5:
    print ('Equals 5')
if x > 4:
    print ('Greater than 4\n')

for i in range (3):
    print (i)
    if i > 1:
        print ('Bigger than 1')
    print ('Done with i =', i,'.')
print ('All done\n')

# en vez de if >10 e if <10  puedes decir que haga una cosa Y SI NO ES ASI OTRA con else
x = input ('Dime un valor de x para comparar si es mayor de 10 y de 20 a la vez: ')
if int(x) < 10:
    print ('Menor que 10.')
elif int(x) < 20:
    print ('Mayor que 10, pero menor que 20.')
else:
    print ('Mayor que 20.')
print ('Finish\n')

# try y except sirven para que el programa intente algo y si da error que haga otra cosa, pero que no se pare al no saber continuar, ej:

astr = 'Hello world'
try:
    istr = int(astr)
except:
    istr = -1

print ('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    print ('Second', istr)

###
astr = input ('Enter a number: ')
try:
    istr = int(astr)
except:
    istr = 'xrbasfasfgasfrwe'

if istr != 'xrbasfasfgasfrwe':
    print ('Nice work')
else:
    print ('Not a number.')