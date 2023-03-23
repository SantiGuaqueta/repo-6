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