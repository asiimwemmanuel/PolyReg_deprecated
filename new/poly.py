import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def fit_polynomial(data_dict, max_degree=4):
    """
    Fits polynomial functions of degrees 0 to max_degree to the given data points
    and chooses the best-fit polynomial based on the coefficient of determination (R²).

    Args:
        data_dict (dict): A dictionary where keys represent the x-values and values represent the corresponding y-values.
        max_degree (int, optional): The maximum degree of the polynomial to consider. Defaults to 4.

    Returns:
        function: A lambda function that represents the best-fit polynomial function.
    """
    x = np.array(list(data_dict.keys()))
    y = np.array(list(data_dict.values()))

    best_model = None
    best_r2 = -np.inf

    for degree in range(max_degree + 1):
        # Create polynomial features
        X_poly = np.vander(x, degree + 1, increasing=True)

        # Fit linear regression model
        model = LinearRegression()
        model.fit(X_poly, y)

        # Predict y values
        y_pred = model.predict(X_poly)

        # Calculate R² score
        r2 = r2_score(y, y_pred)

        if r2 > best_r2:
            best_model = model
            best_r2 = r2

    # Create a lambda function using the best_model
    best_model_func = lambda x: np.polyval(best_model.coef_[::-1], x)

    return best_model_func
