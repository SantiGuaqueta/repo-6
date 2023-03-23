def cantidadDeCarneAves (N:float,M:float,k:float)-> float:
    return (N*6)+(M*7)+(k)
if __name__ == "__main__":
    N=float(input("ingrese la cantidad de gallinas: "))
    M=float(input("ingrese la cantidad de gallos: "))
    k=float(input("ingrese la cantidad de pollitos"))
    cantidadDeCarne= cantidadDeCarneAves(N,M,k)
    print("la cantidad de carne de aves es: "+str(cantidadDeCarne)+"kg")