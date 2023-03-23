def totalContagiados (C:float, D:float)->float:
  return C * (2 ** D)

C = float(input("Ingrese el número actual de contagiados: "))
D = float(input("Ingrese el número de días a partir de hoy: "))
contagiados= totalContagiados(C,D) 
print("El número total de personas contagiadas después de " +str(D)+ " días es: "+str(contagiados))