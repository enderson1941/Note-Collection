import numpy as np
import matplotlib.pyplot as plt


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


axis_x = np.linspace(-20, 20, 160)
fig = plt.figure()


for x in axis_x:  # range(-20, 20, 1)
    val = sigmoid(x)
    plt.plot(x, val, 'o')
plt.show()
