import matplotlib.pyplot as plt
import time, numpy, math, random
# fonction qui retourne le sin de la courbe 
def f(x):
    return numpy.exp(-x/10) * numpy.sin(x)
# les paramètres
a, b = 0, 10
nb_points = 10000
step = (b-a)/nb_points
# list qui stock les valeurs 
x_values, y_values = [], []

x_values = numpy.linspace(a, b, nb_points)
y_values = f(x_values)

for index_point in range(0, nb_points+1):
    numpy.append(x_values, a + index_point*step)
    numpy.append(y_values, f(a + index_point*step))

gradient = numpy.gradient(y_values, x_values)

# moyenne avec slice 
slicing = slice(3000, 7000)
print(y_values[slicing])
sum_y = sum(y_values[slicing])/len(y_values[slicing])
print("la moyenne :",sum_y)
# ecartype
ecart_type = numpy.std(y_values[slicing])
print("l'ecart-type :", ecart_type)
# Lorsque la dérivé f(x) = 0
def f_prime(x) :
    return ((numpy.exp(-x/10.0) + numpy.cos(x)) * ((-0.1 * numpy.exp(-x/10.0)) + numpy.sin(x)))
def dichotomie(f, a, b):
    pas= 1e-6
    while (b - a) > pas:
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2

print("Valeur la plus proche entre l'intervalle[0:3] :",dichotomie(f_prime , 0 , 3))
print("Valeur la plus proche entre l'intervalle[3:6] :",dichotomie(f_prime , 3 , 6))
print("Valeur la plus proche entre l'intervalle[6:10] :",dichotomie(f_prime , 6 , 10))

# methode de monte carlo
def monte_carlo():
    point = random.randint(1,100)
    point_2 = random.randint(1,100)
    if(point == point_2):
        state = True
    else:
        state = False
    return state
num_simulations = 10000
max_points = 1000
plt.figure(figsize=(10,6))
plt.plot(x_values, y_values)
plt.plot(x_values, gradient)

plt.show()