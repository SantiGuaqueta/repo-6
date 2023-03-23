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
    
    
