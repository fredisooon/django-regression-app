from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Generate the data
x1 = np.arange(1, 101)
x2 = np.arange(25, 251, 5)
x3 = np.arange(3, 403, 4)
y = x1 + x2 + np.random.normal(0, 50, size=100)

# Create polynomial features up to degree 2
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(np.column_stack((x1, x2, x3)))

# Fit a linear regression model
reg = LinearRegression().fit(X_poly, y)

# Print the coefficients
print(reg.intercept_)  # should be close to 0
print(reg.coef_)       # should have 6 elements: [coeff_x1, coeff_x2, coeff_x3, coeff_x1x2, coeff_x1x3, coeff_x2x3]
