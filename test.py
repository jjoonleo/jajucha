import math


def f(x, p, r):
    return math.acos((r-x)/r)*r-p


def df(x, r):
    tmp = math.acos((r-x)/r)
    tmp2 = (1/r - (r-3)/r**2)*r
    tmp3 = math.sqrt(1-(r-3)**2/r**2)
    return tmp - (tmp2/tmp3)


p = 10
x = 11
r = 8
for i in range(0, 14):
    tmp = f(x, p, r)
    print(tmp)
    tmp2 = df(x, r)
    print(tmp2)
    r = -(tmp/tmp2) + r
    print(r)
