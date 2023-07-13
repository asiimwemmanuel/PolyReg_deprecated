import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def polytrend(data, points, f_type='auto'):
    # Extract x and y data points from the dictionary
    x_known = np.array(list(data.keys()))
    y_known = np.array(list(data.values()))

    if f_type == 'auto':
        # Perform automatic fitting and selection
        models = {
            'poly': np.polyfit,  # Polynomial fitting
            'exp': lambda x, a, b, c: a * np.exp(b * x) + c,  # Exponential function
            'log': lambda x, a, b, c: a * np.log(b * x) + c,  # Logarithmic function
            'tri': lambda x, a, b, c: a * np.sin(b * x) + c,  # Trigonometric function
            'hyper': lambda x, a, b, c: a / (b * x) + c  # Hyperbolic function
        }

        best_fit = None
        best_type = None
        min_error = float('inf')

        for f_type, model in models.items():
            try:
                # Fit the model to the known data points
                popt, _ = curve_fit(model, x_known, y_known)
                # Calculate the y values for the given points using the fitted model
                y_calculated = model(points, *popt)
                # Calculate the sum of squared errors between known and calculated y values
                error = np.sum((y_known - model(x_known, *popt)) ** 2)
                if error < min_error:
                    min_error = error
                    best_fit = y_calculated
                    best_type = f_type
            except (RuntimeError, TypeError):
                continue

        f_type = best_type
        y_calculated = best_fit

        if f_type is None:
            raise ValueError("No suitable function found to fit the data.")

    else:
        model = {
            'poly': np.polyfit,
            'exp': lambda x, a, b, c: a * np.exp(b * x) + c,
            'log': lambda x, a, b, c: a * np.log(b * x) + c,
            'tri': lambda x, a, b, c: a * np.sin(b * x) + c,
            'hyper': lambda x, a, b, c: a / (b * x) + c
        }.get(f_type)

        if model is None:
            raise ValueError("Invalid function type provided.")

        # Fit the specified function type to the data
        popt, _ = curve_fit(model, x_known, y_known)
        # Calculate the y values for the given points using the fitted model
        y_calculated = model(points, *popt)

    # Plot the known data points and the calculated data points
    plt.title('PolyTrend')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(x_known, y_known, 'ro', label='Known Data')
    plt.plot(points, y_calculated, 'b-', label='Calculated Data')
    plt.legend()
    plt.show()

# Example usage:
data = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
points = [6, 7, 8]

polytrend(data, points, 'poly')
