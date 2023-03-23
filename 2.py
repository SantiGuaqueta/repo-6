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