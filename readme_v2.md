modify the script so that the best curve fit model is made and can be called via a funciton, and use ridge regression. here's an example with polynomial regression:

# selecting best model
best_deg = potent_degs[np.argmin(mse_values)]
coeffs = np.polyfit(x, y, best_deg)
polynomial = np.poly1d(coeffs)
