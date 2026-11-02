import math
import matplotlib.pyplot as plt

x1 = 0.8
x2 = 0.4
neurons = [[0.6, -0.2, 0.1], [0.3, 0.5, -0.1], [-0.4, 0.8, 0.2]]
target = 0.9
learning_speed = 0.1
y = 0

def ponderate_sum(x1, x2, w1, w2, b):
    z = (x1 * w1) + (x2 * w2) + b
    return z

def sigmoide(z):
    sigmoide = 1 / (1 + (math.e ** (-1 * z)))
    return sigmoide

def error(t, y):
    error = (1/2)*(t-y)**2
    return error

def derivate_e_w1(z):
    y = sigmoide(z)
    derivate = y*(y-target)*(1-y)*x1
    return derivate

def derivate_e_w2(z):
    y = sigmoide(z)
    derivate = y * (y - target) * (1 - y) * x2
    return derivate

def derivate_e_b(z):
    y = sigmoide(z)
    derivate = y * (y - target) * (1 - y)
    return derivate

def correction(w1, w2, b, z):
    w1 = w1-learning_speed * derivate_e_w1(z)
    w2 = w2 - learning_speed * derivate_e_w2(z)
    b = b - learning_speed * derivate_e_b(z)
    return w1, w2, b

errors = []
"""for i in range(1000):
    z = ponderate_sum(x1, x2, w1, w2, b)
    y = sigmoide(z)
    errors.append(error(target, y))
    w1, w2, b = correction(w1, w2, b, z)
print(w1, w2, b, y)


plt.title("Evolution des erreurs")
plt.xlabel("Nombre d'itération")
plt.ylabel("Pourcentage d'erreur")
plt.plot(errors)
plt.show()"""

for i in range(0, 3):
    for j in range(0, 3)