#entradas

edad1=int(input('ingrese la edad del primer usuario: '))
edad2=int(input('ingrese la edad del segundo usuario: '))
edad3=int(input('ingrese la edad del tercer usuario: '))

#procesos

if edad1<0 or edad2<0 or edad3<0:
    print('Alguna es incorrecta: negativa')
    
else:
    print('Todas son correctas')
    