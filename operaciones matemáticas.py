import math
x = float(input("Ingrese un numero valor para X: "))

y1 = (2*x)+5
print("y1 es igual a: ",y1)

y2 = (3*y1)-4
print("y2 es igual a: ",y2)

y3 = math.sqrt((y2)-(y1))
print("y3 es igual a: ",y3)

y4 = (y3*y1) / (2+y2)
print("y4 es igual a: ",y4)

y5 = (y4+y3)-(y2*y1)
print("y5 es igual a: ",y5)

y6 = ((((math.e)**y5)*math.sin(y1))/(math.log10(y2+y3)*math.cos(y4)+1.5))
print("y6 es igual a: ",y6)