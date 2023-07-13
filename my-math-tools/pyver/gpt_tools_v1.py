from typing import List, Union
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial

class gpt:
    @staticmethod
    def gpt_alg_v0(data: List[float], n: Union[int, bool] = False) -> Union[float, None]:
        if n == True:
            # return a polynomial fit instead of a float
            x = np.array(list(range(1, len(data) + 1)))
            y = np.array(data)
            poly = lagrange(x, y)
            return Polynomial(poly.coef[::-1])

        if n <= 0:
            return None

        elif n <= len(data):
            return float(data[n - 1])

        x = np.array(list(range(1, len(data) + 1)))
        y = np.array(data)
        poly = lagrange(x, y)
        return round(Polynomial(poly.coef[::-1])(n), 2)
