import math

x1 = 0.8
x2 = 0.4
w1 = [0.6, 1.0, 2.0]
w2 = -0.2
b = 0.1

def ponderate_sum(x1, x2, w1, w2, b):
    z = (x1 * w1) + (x2 * w2) + b
    return z

def sigmoide(z):
    sigmoide = 1 / (1 + (math.e ** (-1 * z)))
    return sigmoide

for ele in w1:
    x = ponderate_sum(x1, x2, ele, w2, b)
    print(x, " ", sigmoide(x))