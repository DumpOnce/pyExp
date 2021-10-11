from matplotlib import *
import matplotlib.pyplot as plt
import numpy


def main():
    x = numpy.linspace(0, 100, 110)
    y = x**(-3)
    plt.title("linear function")

    plt.plot(x, y)
    plt.show()


if  __name__ == "__main__":
    main()
