import numpy as np
import scipy
from liba import Reading


def main():
    a = Reading('imageTest.json', 100, 200)
    a.read()


if __name__ == "__main__":
    main()
