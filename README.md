# Portafolio de Fundamentos de programacion
# ¿Qué es Python?
Python es un lenguaje de programación interpretado que lo hace sencillo de leer y escribir. Es multiparadigma, permite varios estilos además otros paradigmas están soportados mediante el uso de extensiones.
```Python
print(“Hola podemos ser amigos”)
print(“Si o No”)
respuesta=input()
```

# ¿Qué es una variable?
Se la define como el espacio reservado de memoria que almacena un dato, una variable puede cambiar de valor en tiempo de ejecución.
Podemos imaginar a una variable como una cajita que almacena dato. 
```Python
nombre= “Allisson Huilca”
edad= 20
print(“Mi nombre es: ”) 
print(nombre)
print(“Mi edad es: ”)
print(edad)
[output]
Mi nombre es:
Allisson Huilca 
Mi edad es:
20
```
## Nombrando una variable
Las variables tienen nombres y estas siguen reglas puede contener números, letras o carácter `_`.
Se debe elegir  un nombre significativo que tenga relación con el dato que representará. Se debe mantener consistencia en el estilo a utilizar en nombres que contengan más de una palabra.
```
dato1
result_2
consumo_total
nombre
```

No debe iniciar con un número, no debe iniciar con mayúsculas, el nombre no debe ser muy largo manteniendo un máximo de 15 caracteres. 
```
1total
Edad
Total-por-pagar-sin-iva
```

No debe usar una palabra reservada del lenguaje, porque estas palabras ya tienen un significado gramatical especial.

```
and, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, input, is, lambda, next, not, or, pass, print, raise, return, try, while, yield.
```

## Asignando valores a una variable
El operador de asignación es el signo `=` . Se utiliza para crear variables y asignar un valor, se la escribe de derecha a izquierda y si la variable a sido creada anteriormente, se puede modificar su contenido con el mismo operador.
```Python
x = 15
y = 25

x= 100
y = 225
```
También existen otras asignaciones como:
`Asignación en la misma línea `
```Python
x= 6;   y=10;   z= 3
```
`Asignación múltiple`
```Python
day, month, year= “martes”, “marzo”, 2001
```
`Asignación del mismo valor`
```Python
base = altura = 6
```
`Asignación de intercambio`
```Python
base= 13, altura= 55
base, altura= altura, base
```

## Operadores básicos
Existen operadores aritméticos, relacionales, lógicos, de incremento y decremento.

`Operadores Aritméticos`
Se pueden utilizar paréntesis `()` para definir el orden de las operaciones

### Suma
Este operador usa el simbolo `+` :
```Python
suma = 18 + 20
print(suma)
[output] 38
```
Tambien se puede asignar valores a variables y sumar esas variables:
```Python
x = 6
y = 18
suma = x + y
print(suma)
[output] 24
```
Y por supuesto se puede sumar mas de dos variables:
```Python
x = 14 
y = 4
z = 10
suma = x + y + z
print(suma)
[output] 28
```
### Resta
Este operador tiene como signo al `-` :
```Python
x = 10
y = 5
resta = x - y
print(resta)
[output] 5
```
### Multiplicación
### División
### Módulo

 
`Operadores Relacionales`
Estos símbolos se utilizan para comparar valores, su resultado siempre será un valor lógico `True o False`
Tenemos los símbolos:

`== : Igual que`
```Python
4 == 4
[output] True
```

`!= : Distinto que`
```Python
9 != 3
[output] True
```

`> : Mayor que`
```Python
4 > 7
[output] False
```

`< : Menor que`
```Python
10 > 3
[output] False
```

`>= : Mayor o igual que`
```Python
8 >= 5
[output] True
```

`<= : Menor  o igual que`
```Python
7 >= 1
[output] False
```

`Operadores Relacionales`
Permiten construir expresiones lógicas, obteniendo como resultado valores lógicos. Tenemos los símbolos:

`and : Conjunción`
```Python
2 >1 and 4 < 8
[output] True
```

`or : Disyunción`
```Python
9 != 6 or 7 <= 3
[output] True
```

`not : Negación`
```Python
not True
[output] False
```

`Operadores de Incremento y Decremento`
Estos operadores son asignaciones con operadores porque están combinados con el símbolo `=`. Tenemos los símbolos:

`+=`
```Python
a+=5
[Equivalente a ] a=a+5
```

`-=`
```Python
a-=5
[Equivalente a ]   a=a-5
```

`*=`
```Python
a*=5
[Equivalente a ]   a=a*5
```

`/=`
```Python
a/=5
[Equivalente a ]  a=a/5
```

`%=`
```Python
a%=5
[Equivalente a ]  a=a%5
```
Nota:
Hay que tener en cuenta la prioridad de Operadores:
```
Paréntesis
Potencia 
Multiplicación y división 
Suma y resta 
Operadores de igual procedencia y se evalúan de derecha a izquierda
```
# Tipos de datos en Python
## Integer
## Float
## String
## Casting en Python
## List
## Tuple
## Dictionary
# Tomando decisiones
## Sentencia if
## Ciclo For
## Ciclo While
## Break
## Continue
