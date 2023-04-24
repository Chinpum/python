# ENTRADAS
cat=input('Por favor ingrese la categoria: ')
imp=float(input('Por favor ingrese el importe: '))

# PROCESOS

if cat=='a' and imp>=5000:
    descuento=imp-(imp*5)/100
    print('El importe a pagar por el cliente es: ', descuento)
    
elif cat=='b' and imp>2500 and imp<3800:
    descuento=imp-(imp*2)/100
    print('El importe a pagar por el cliente es: ', descuento)