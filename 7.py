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
