import matplotlib.pyplot as pyplot
import MainSimplexeInitial

Y = []
X = []
for i in range(20):
    X.append(2 + 2* i)
    Y.append(MainSimplexeInitial.main_simplexe_initial(2 + 2* i, 1))

print(X, Y)
pyplot.plot(X, Y)
pyplot.show()
