import numpy as np
import matplotlib.pyplot as plt
from typing import List, Union

def find_nth_term(lst: List[float], n: Union[int, str]) -> Union[float, str]:
    if isinstance(n, int):
        if n <= 0:
            return "n must be 1 or greater."
        elif n <= len(lst):
            return lst[n-1]
        else:
            x = np.arange(1, len(lst)+1)
            y = np.array(lst)
            coeffs = np.polyfit(x, y, len(lst)-1)
            return np.polyval(coeffs, n)
    elif isinstance(n, str):
        if n == 'exp':
            x = np.arange(1, len(lst)+1)
            y = np.array(lst)
            coeffs = np.polyfit(x, y, len(lst)-1)
            exp_str = ""
            for i, coeff in enumerate(coeffs[::-1]):
                if i == 0:
                    exp_str += f"{coeff:.2f}"
                elif i == 1:
                    exp_str += f" + {coeff:.2f}n"
                else:
                    exp_str += f" + {coeff:.2f}n^{len(coeffs)-i}"
            return exp_str
        elif n == 'graph':
            x = np.arange(1, len(lst)+1)
            y = np.array(lst)
            coeffs = np.polyfit(x, y, len(lst)-1)
            x_new = np.linspace(1, len(lst), num=50)
            y_new = np.polyval(coeffs, x_new)
            plt.plot(x, y, 'o', x_new, y_new)
            plt.title("Fitted polynomial")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.show()
            return
    else:
        return "Invalid second parameter."

