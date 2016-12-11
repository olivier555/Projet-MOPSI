import matplotlib.pyplot as pyplot
import statistics
import MainSimplexeInitial

Y = []
X = []
ecart_type_Y = []
nb_iter = 1
for i in range(12):
    X.append(2 + 2* i)
    liste =[]
    for j in range(nb_iter):
        liste.append(MainSimplexeInitial.main_simplexe_initial(2 + 2 * i, 1))
    Y.append(statistics.mean(liste))
    #ecart_type_Y.append(statistics.stdev(liste))

print(X, Y, ecart_type_Y)
pyplot.plot(X, Y)
pyplot.show()
