import matplotlib.pyplot as plt
import numpy as np

# draw y = ax + b
def draw_linear_graph(x, a, b):
    y = [(a * num + b) for num in x]
    return y

x = np.arange(-1, 4, 0.1)

# indeterminate linear equation
plt.plot(x, draw_linear_graph(x, -1, 1),
         x, draw_linear_graph(x, 1, -1),
         x, draw_linear_graph(x, 1/3, 1))

plt.show()
