#Amaya Galaviz Maribel
#IA_Practica 2 Unidad 2 datos vino
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Definición de la clase Perceptrón
class Perceptron(object):
    def __init__(self, eta=0.01, n_iter=10):
        # Inicialización de la tasa de aprendizaje y el número de iteraciones
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        # Inicialización de pesos y lista para almacenar errores en cada iteración
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                # Actualización de pesos según regla de aprendizaje del perceptrón
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        # Cálculo de la entrada neta
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        # Predicción de la clase
        return np.where(self.net_input(X) >= 0.0, 1, -1)

# Lectura de datos desde una URL
df = pd.read_csv('winequality.csv', header=None)

# Selección de las clases de vino
y = df.iloc[0:6497, 4].values
y = np.where(y == 'wine-quality', -1, 1)

# Extracción de características de acidez y de dioxido de azufre
X = df.iloc[0:6497, [0, 2]].values

# Representación gráfica de los datos
plt.scatter(X[:1599, 0], X[:1599, 1],
            color='red', marker='o', label='red')
plt.scatter(X[1599:6497, 0], X[1599:6497, 1],
            color='blue', marker='*', label='white')

plt.xlabel('Acidez')
plt.ylabel('Dioxido de azufre')
plt.legend(loc='upper left')
plt.show()
