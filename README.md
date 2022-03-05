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
Este operador usa el signo `*`:
```Python
x= 8
y= 5
multiplicacion = x * y
print(multiplicacion)
[output] 40
```

### División
Este operador usa el signo `/`:
```Python
x = 18
y = 9
division = x / y
print(division)
[output] 2
```

Tambien existe la division entera su símbolo es `//`:
```Python
x= 78
y = 2
div_entera= x // y
print(div_entera)
[output] 6
```

### Módulo
Este operador usa el símbolo `%` se usa asi:
```Python
x = 18
y = 7
modulo = x % y
print(modulo)
[output] 4
 ```
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
Son la representacion de los números enteros `int` ya sean positivos o negativo
```Python
nun_1= 100
num_2= 34
```
## Float
Son la representacion de los números enteros o flotantes `float`  
```Python
nun_1= 10.3
num_2= 5.9
```
## String
Son la representación de caracteres que forman palabras y se representan por comillas simples `' '` o dobles `" "`
```Python
print("Hola")
nombre = "Allisson"
print("nombre")
```
## Casting en Python
Es aquello que sirve y se utiliza para convertir un tipo de dato a un dato totalmente diferente osea:
```Python
int a str: str(65)
str a int: int("1034")
float a int: int(3.5)
```
## List
List en python son variables que almacenan varios tipos de datos en orden
```Python
lista_compras = ["carne", "pan", "queso", "pollo", 12, 21, 36]
print(lista_compras)
[output] [carne, pan, queso pollo, 12, 21, 36]
```
## Tuple
Es un conjunto ordenado e inmutable de elementos del mismo o diferente tipo.
```Python
(1, "a", 1.1, 2, "b", 2.2).
print(ejemplo)
[output] (1, a, 1.1, 2, b, 2.2)
```
## Dictionary
Los diccionarios en python son un tipo de dato que se categoriza como una "colección" el cual permite guardar elementos (Clave:Valor). Estos elementos se declaran con llaves {} y se separan con comas , y cada elemento se define con su palabra clave, este debe ser un dato no mutable y un valor cualquiera:
```Python
#se usa de la siguiente manera:
dic1={ }

#aqui creamos uno con claves y valores
dicCantidad={"banana":50,"mango":2,"sandia":15}
```
# Tomando decisiones
## Sentencia if
IF es una estructura de control que ejecuta el programa cuando se cumpla cierta condición de dato Booleano.

## Ciclo For
El cual es una estructura de control que nos permite repetir sentencias(una serie de instrucciones) un número determinado de veces

°Al usar un ciclo for tambien usaremos la función range que nos permitira controlar el números de ciclos o veces que interactue el bucle for.
## Ciclo While
El ciclo while es una estructura de control o de repetición, que inician o repiten un bloque de instrucciones si se cumple una condicion o mientras se cumple cierta condicion.
## Break
La instrucción break le proporciona la oportunidad de cerrar un bucle cuando se activa una condición externa. Debe poner la instrucción break dentro del bloque de código bajo la instrucción de su bucle, generalmente después de una instrucción if condicional. 
## Continue
El uso de continue al igual que el ya visto break, nos permite modificar el comportamiento de de los bucles while y for. La diferencia entre el break y continue es que el continue no rompe el bucle, si no que pasa a la siguiente iteración saltando el código pendiente.
