# Ejercicio Integer_3
#calcular la suma y la media aritmetica N numeros reales. Solicitar el valor de N al usuario
#y cada uno de los numeros reales

n= int(input("Ingrese numero:"))
suma=0
for i in range(n):
    numero=int(input("Ingrese un valor:"))
    suma= suma+numero

print("Suma total:", suma)
media =suma/n
print("La media aritmetica es:", media)
