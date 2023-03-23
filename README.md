

# Reto #6
## 1. Dado la figura de la imagen, desarrolle:
+ Una función matemática para calcular el área superficial y el volumen.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r1`, `r2` y `h`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

![Captura de pantalla 2023-03-22 172132](https://user-images.githubusercontent.com/124614680/227052258-3a8a9f95-40d9-4605-a259-da4822c8334a.png)


```pseudocode
import math
def volumenAreaFigura(radio1:float, radio2:float,altura:float) -> float:
  volumen = (4/3 * math.pi * (radio1**3) ) + ((math.pi * radio2 * radio2 * altura) / 3)
  area= (math.pi * radio2**2 + math.pi * radio2 * (altura**2 + radio2**2)** 0.5 ) + (4* radio1 * radio1 * math.pi)
  return (volumen,area)

if __name__ == "__main__":
  radio1 = float(input("Ingrese el radio de la esfera:"))
  radio2 = float(input("Ingrese el radio del cono:"))
  altura = float(input("Ingrese altura del cono:"))
  volumen,area = volumenAreaFigura(radio2,radio1, altura)
  print("El area de la figura es " + str(area))
  print("el volumen de la figura es " +str(volumen))
```
Primero llamamos la función math de la siguiente manera: `import math` esto con el objetivo de sacar el valor de pi (`math.pi`) de este paquete,  definimos la función para allar el volumen y el área superficial, aplicamos las formulas a la esfera y luego al cono y las sumamos, esto lo hacemos en ambos casos (para hallar el área y el volumen), pedimos que nos devuelva ambas variables cerrando así nuestra función.
Luego le pedimos a nuestro usuario que digité los valores que necesitamos para hallar el area y volumen, llamamos nuestra función, y finalmente imprimimos los resulltados.

## 2.Dado la figura de la imagen, desarrolle:
![Captura de pantalla 2023-03-22 174604](https://user-images.githubusercontent.com/124614680/227055212-1397f3d6-d387-4eac-8473-570bff106cc8.png)

+ Una función matemática para calcular el área y el perimetro.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*
```pseudocode
import math
def perimetroAreaFigura(radio:float, base:float, altura:float) -> float:
  perimetro= (2*(2*radio*math.pi)) + (2*(base*altura))
  area= (math.pi * (radio**2)) + (base * altura)
  return  (perimetro,area)
if __name__ == "__main__":
  radio = float(input("Ingrese el radio de lal círculo:"))
  base = float(input("Ingrese la base del rectangulo:"))
  altura = float(input("Ingrese altura del rectangulo:"))
  area, perimetro = perimetroAreaFigura(radio, altura,base)
  print("El area de la figura es " + str(area))
  print("el perimetro de la figura es " +str(perimetro))
```
Primero llamamos la función math de la siguiente manera: `import math` esto con el objetivo de sacar el valor de pi (`math.pi`) de este paquete, definimos la función para allar el volumen y el perimetro, aplicamos las formulas a los circulos y luego al rectangulo y las sumamos, esto lo hacemos en ambos casos (para hallar el área y el perimetro), pedimos que nos devuelva ambas variables cerrando así nuestra función. Luego le pedimos a nuestro usuario que digité los valores que necesitamos para hallar el area y el perimetro, llamamos nuestra función, y finalmente imprimimos los resulltados.
 
### 3.Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```pseudocode
def cantidadDeCarneAves (N:float,M:float,k:float)-> float:
    return (N*6)+(M*7)+(k)
if __name__ == "__main__":
    N=float(input("ingrese la cantidad de gallinas: "))
    M=float(input("ingrese la cantidad de gallos: "))
    k=float(input("ingrese la cantidad de pollitos"))
    cantidadDeCarne= cantidadDeCarneAves(N,M,k)
    print("la cantidad de carne de aves es de : "+str(cantidadDeCarne)+"kg")
```
Primero definimos nuestra función donde vamos a multiplicar las variables por el peso correspondiente, devolvemos esta formula, y le pedimos a nuestro usuario que digite las aves correspondientes, llamamos nuestra función antes creada e imprimimos la cantidad de carne total en kilos.

#### 4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```pseudocode
def costo(pan:float, huevos:float, leche)-> float:
    valor= (pan*300) + (leche*3300) + (huevos*350)
    return valor
if __name__ == "__main__":
    pesos= float(input("ingrese el valor del billete: ")) 
    pan= float(input("ingrese la cantidad de panes: "))
    huevos= float(input("ingrese la cantidad de huevos:"))
    leche= float(input("ingrese la cantidad de leche:"))
    valor= costo(pan,huevos,leche)
    p = pesos - valor 
    if pesos > valor:
     print("Sus vueltas son " +str(p)+ " pesos")
    if valor > pesos:
     print("Usted debe " +str(-p)+ " pesos")
```
Creamos la funcion donde multiplicamos el el valor por sus variables respectivas y pedimos que nos devuelva ese valor, indicamos a nuestro usuario que digite la cantidad de alimentos que vamos a comprar de cada uno, y el valor del billete que tenemos, donde si el billete que tenemos es menor que el costo de las cosas que compramos, nos dira que quedamos debiendo ese dinero, y si por el contrario es mayor el billete, nos arrojara el dato de las vueltas que debemos recibir.

### 5. Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.
```pseudocode
def calculoPrestamo(C:float, i:float, n:float)->float:
   valor = C * (1 + ((i/100)/12))**n
   return valor

if __name__ == "__main__":
    C = float(input("ingrese el valor del prestamo inicial: "))
    i = float(input("ingrese la tasa de interes: "))
    n = float(input("ingrese el numero de meses: "))
    valorFinal = calculoPrestamo(C, i, n)

print(f"El valor del préstamo después de " +str(n) + " meses es de: " +str(valorFinal))
```
Creamos la funcion que nos calculara el valor final del prestamo, esto a través de la formula de interes compuesto "C * (1 + ((i/100)/12))**n", le pedimos al usuario que digite las variables que indicamos para hacer uso de nuestra formula y así imprimir el valor del prestamo final en un número de meses especificados por el usuario.
### 6 El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
```pseudocode
def totalContagiados (C:float, D:float)->float:
  return C * (2 ** D)

C = float(input("Ingrese el número actual de contagiados: "))
D = float(input("Ingrese el número de días a partir de hoy: "))
contagiados= totalContagiados(C,D) 
print("El número total de personas contagiadas después de " +str(D)+ " días es: "+str(contagiados))
```
Creamos nuestra función totalContagiados donde multiplicamos la variable de contagiados por 2 elevado al el numero de dias que transcurre, esto para que se duplique dia a dia. pedimos a nuestro usuarioque digite los contagiados actuales y el numero de dias que transcurriran, llamamos nuestra función,y el programa nos devolvera el numero total de contagiados transcurridos los dias.

### 7 Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número
  ```pseudocode
  def mediana (num1:float, num2:float, num3:float, num4:float, num5:float)->float:
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num3 > num4:
        num3, num4 = num4, num3
    if num4 > num5:
        num4, num5 = num5, num4
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num3 > num4:
        num3, num4 = num4, num3
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num2:
        num1, num2 = num2, num1

    return num3

def promedio (num1:float, num2:float, num3:float, num4:float, num5:float)->float:
    P= (num1+num2+num3+num4+num5)/5
    return P

def promedioMultiplicativo (num1:float, num2:float, num3:float, num4:float, num5:float)->float:
    PM= (num1*num2*num3*num4*num5)**(1/5)
    return PM
 
def ordenarNumerosAscendete(num1:float, num2:float, num3:float, num4:float, num5:float)->float:
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num3 > num4:
        num3, num4 = num4, num3
    if num4 > num5:
        num4, num5 = num5, num4
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num3 > num4:
        num3, num4 = num4, num3
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num2:
        num1, num2 = num2, num1

    return num1, num2, num3, num4, num5

def ordenarNumerosDescendete (num1:float, num2:float, num3:float, num4:float, num5:float)->float:
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num3 > num4:
        num3, num4 = num4, num3
    if num4 > num5:
        num4, num5 = num5, num4
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num3 > num4:
        num3, num4 = num4, num3
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num2:
        num1, num2 = num2, num1

    return num5, num4, num3, num2, num1

def potencia (num1:float, num2:float, num3:float, num4:float, num5:float)->float:
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num3 > num4:
        num3, num4 = num4, num3
    if num4 > num5:
        num4, num5 = num5, num4
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num3 > num4:
        num3, num4 = num4, num3
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num2:
        num1, num2 = num2, num1

    return (num5)**(num1)

def raizCubica (num1:float, num2:float, num3:float, num4:float, num5:float)->float:
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num3 > num4:
        num3, num4 = num4, num3
    if num4 > num5:
        num4, num5 = num5, num4
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num3 > num4:
        num3, num4 = num4, num3
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num2:
        num1, num2 = num2, num1

    return (num1)**(1/3)
    
   ```   
Primero hacemos en un archivo todas las funciones con las ecuaciones que necesitamos para hacer funcionar el programa.
```pseudocode
from Funciones import mediana 
from Funciones import promedio 
from Funciones import promedioMultiplicativo 
from Funciones import ordenarNumerosAscendete 
from Funciones import ordenarNumerosDescendete
from Funciones import potencia
from Funciones import raizCubica
if __name__ == "__main__":
 num1 = float(input("Ingrese el primer número: "))
 num2 = float(input("Ingrese el segundo número: "))
 num3 = float(input("Ingrese el tercer número: "))
 num4 = float(input("Ingrese el cuarto número: "))
 num5 = float(input("Ingrese el quinto número: "))
 m = mediana(num1,num2, num3, num4, num5)
 p= promedio(num1,num2,num3,num4,num5)
 pm= promedioMultiplicativo(num1,num2,num3,num4,num5)
 oa= ordenarNumerosAscendete(num1,num2,num3,num4,num5)
 od= ordenarNumerosDescendete(num1,num2,num3,num4,num5)
 pot= potencia(num1,num2,num3,num4,num5)
 r= raizCubica(num1,num2,num3,num4,num5)
print("El promedio es:" +str(p))
print("La media es:" +str(m))
print ("El promedio multiplicativo: " +str(pm))
print ("Los numeros ordenados de forma ascendente son:"+str(oa))
print ("Los numeros ordenados de forma descendente son:" +str(od))
print ("La potencia del número mayor elevado al menor es: " +str(pot))
print ("La raíz cúbica del menor número es: " +str(r))
```
Luego importamos cada una de las funciones que necesitamos desde el otro archivo esto con `from "elNombreDelArchivo" import "elNombreDeLaFuncion"`, y las llamamos en nuestro programa, también hacemos que el usuario digite los números que se utilizaran y se calcularan, para que finalmente el programa imprima cada una de las cosas que le pedimos anteriormente.
