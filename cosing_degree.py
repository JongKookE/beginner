import math 

b1 = 180
b2 = 165
c1=115
a1 = 120
a2 = 100


a = b1**2 + c1**2 - 2*b1*math.cos(a1)

def formula(b1,b2,c1,A1,A2):
    a = b1**2 + c1**2 - 2*b1*c1*math.cos(A1)
    return a

# print(formula(b1,b2,c1,a1,a2)**0.5)

print(math.cos(a1))



