
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