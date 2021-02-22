'''
#task 1.1
from cmath import log, sqrt

x=int(input("Enter x: "))
y=int(input("Enter y: "))
a=pow(y,5)+52*(pow(y,7))
b=((pow(y,6))/18)-(3*pow(y,5))
c=(pow(y,8)-log(x)-39)/(51*pow(x,8)+log(x))
d=sqrt(pow(y,6)+35*x)
f=a/b-c+d
print("f (", x, ",", y,") = ", f)
'''

'''
#task 1.2
from cmath import tan, cos, sin

x=int(input("Enter x: "))
if x<120:
    f=tan(pow(x,5))-82*(pow(x,2))
if 120<=x<220:
    f=17*pow((30*(pow(x,8))-(pow(x,6)/68)),8)+68*pow(x,4)
if x >=220:
    f=abs(cos(x)+tan(x))-tan(sin(x)+pow(x,6))
print("f(", x, ") = ", f)
'''

'''
#task 1.1
from cmath import tan, sin

def f1(n,m):
    z=50*(p1(n))+p2(n,m)
    return z
def p1(n):
    x=0
    for i in range(1,n):
        x=x+(tan(i)-82*(pow(i,6)))
    return x;

def p2(n,m):
    y=0
    e=2.718
    for i in range(1,n):
        for j in range(1, m):
            y=y+(sin(j)-pow(e,j))
    return y


print(f1(94,57))
'''

'''
#task 1.1

n=int(input("Enter n:"))
def f1(n):
    if n == 0:
        return 10
    elif n == 1:
        return 4
    else:
        return ((1/97)*(f1(n-1))+(1/79)*(pow(f1(n-1),2)))
print("{:.2e}".format(f1(n)))
'''