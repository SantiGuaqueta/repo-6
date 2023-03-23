def calculoPrestamo(C, i, n):
   valor = C * (1 + ((i/100)/12))**n
   return valor

if __name__ == "__main__":
    C = float(input("ingrese el valor del prestamo inicial: "))
    i = float(input("ingrese la tasa de interes: "))
    n = float(input("ingrese el numero de meses: "))
    valorFinal = calculoPrestamo(C, i, n)

print(f"El valor del préstamo después de " +str(n) + " meses es de: " +str(valorFinal))
