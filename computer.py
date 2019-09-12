import sys

from parser import parser
from process import process_equation

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


"""
Examples:
5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0
4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
5 * X^0 + 4 * X^1 = 4 * X^0
1 * X^0 + 4 * X^1 = 0
8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0
5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0
5 + 4 * X^0 + X^2= X^2
0*X^2-5*X^1-10*X^0=0
X2-5X-10=0
5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0
- 5 * X^0 + 4 * X^1 = 4 * X^0
 8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^2 * 5 = 3 * X^0 + 5X / -2 +5  - -5 -9 - 70
8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^2 * 5 = 3 * X^0 + 5X / - 2 +5  - -5 -9 - 70

Bonus: - color
       - graph avec numpy
       - explication du code ligne par ligne
       - comprehension de l'equation a l'ecrit
       - fraction irreductible
"""


def graph_drawer(a, b, c):
    x = np.arange(-5, 5, 0.25)
    y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(x, y)
    F = a * X * X + b * X + c

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, F)
    plt.show()


if __name__ == "__main__":
    parsed_equations_list, graph = parser()

    graph_value = []
    for i, parsed_equation in enumerate(parsed_equations_list):
        graph_value.append(process_equation(parsed_equation))
        if i < len(parsed_equations_list) - 1:
            print("\n\n")
    if graph:
        for g in graph_value:
            graph_drawer(g[0], g[1], g[2])
