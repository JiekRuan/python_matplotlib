import matplotlib.pyplot as plt
import time, numpy, math
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
print(sum_y)
# ecartype
ecart_type = numpy.std(y_values[slicing])
print(ecart_type)
# Lorsque la dérivé f(x) est null




plt.figure(figsize=(10,6))
plt.plot(x_values, y_values)
plt.plot(x_values, gradient)
plt.show()