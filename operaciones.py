import math



def sumacplx(a,b):
    return ((a[0]+b[0]),(a[1]+b[1]))

def multcplx(a,b):
    return (((a[0]*b[0])-(a[1]*b[1])),a[0]*b[1]+ a[1]*b[0])

def restcplx(a,b):
    return ((a[0]-b[0]),(a[1]-b[1]))

def divcplx(a,b):
    return ((a[0]*b[0]+a[1]*b[1])/(b[0]**2+b[1]**2),(a[1]*b[0]-a[0]*b[1])/(b[0]**2+b[1]**2))

def modcplx(a):
    return((a[0]**2 + a[1]**2)**(1/2))


def conjucplx(a):
    return((a[0],-1*a[1]))

def fasecplx(a):
    return math.atan2(a[1],a[0])

def carteapola(a):
    return (modcplx(a),fasecplx(a))

def polacart(a):
    return (a[0]*math.cos(a[1]),a[0]*math.sin(a[1]))


if __name__ == "__main__":
    print(sumacplx((9.3,2.5),(-6.5,2)))
    print(multcplx((3.5,6),(-6.7,2)))
    print(restcplx((2.5,7),(-1.7,3.4)))
    print(divcplx((-12,6.5),(-7.2,3.9)))
    print(modcplx((-10,2)))
    print(fasecplx((-9.5,4.5)))
    print(conjucplx((-7.5,-2)))
    print(carteapola((-9.4,3.4)))
    print(polacart((9.99599919967984, 2.7945310500503027)))
    

    