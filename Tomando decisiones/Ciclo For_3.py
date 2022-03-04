#calcular e imprimir la tabla de multiplicar de un numero cualquiera. Imprimir el multiplicando, el multiplicador y el producto.

numero = int (input ("Ingrese un numero:"))

for tabla in range (1, 13):
    resultado = tabla * numero

    print(numero,"por",tabla,"es igual a:",resultado)
