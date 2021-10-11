from matplotlib import *
import matplotlib.pyplot as plt
import numpy
import math

def main():
    x = numpy.linspace(0, 100, 110)
    y = x**(-3)
    plt.title("linear function")

   # plt.plot(x, y)

    #y2 = numpy.log(2, x)
    y2 = [i**4 for i in x]
    plt.plot(x, y, x, y2)
    plt.show()


if  __name__ == "__main__":
    main()
