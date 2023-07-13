# this code was obtained from this source: https://youtu.be/H8kocPOT5v0
# it's used as inspiration for polytrend

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

x = 4 * np.random.rand(100, 1) - 2
y = 4 + 2 * x + np.random.randn(100, 1)

poly_features = PolynomialFeatures(degree=1, include_bias=False)
x_poly = poly_features.fit_transform(x)

reg = LinearRegression()
reg.fit(x_poly, y)

x_vals = np.linspace(-2, 2, 100).reshape(-1, 1)
x_vals_poly = poly_features.transform(x_vals)

y_vals = reg.predict(x_vals_poly)

plt.scatter(x, y)
plt.plot(x_vals, y_vals, color='r')
plt.savefig('fig.png')