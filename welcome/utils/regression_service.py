import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd


def simple_linear_regression(request):
    
    indepVar = request.POST.getlist('listOfCheckboxes[]')
    depVar = request.POST.getlist('listOfRadio[]')

    df = pd.read_csv('welcome/media/data.csv')

    X = np.array((df[indepVar[0]])).reshape((-1, 1))
    Y = np.array((df[depVar[0]]))

    model = LinearRegression().fit(X, Y)

    return {'status': 'simple_linear',
            'coef': model.coef_.tolist(),
            'intercept': model.intercept_,
            'R square': model.score(X, Y)}


def simple_polynominal_regression(request):
    print('Inside Polynom calc')
    indepVar = request.POST.getlist('listOfCheckboxes[]')
    depVar = request.POST.getlist('listOfRadio[]')
    
    df = pd.read_csv('welcome/media/data.csv')

    X = np.array((df[indepVar[0]])).reshape((-1, 1))
    Y = np.array((df[depVar[0]]))

    poly = PolynomialFeatures(degree=int(request.POST['polynom_degree']),
                              include_bias=False)
    poly_features = poly.fit_transform(X)

    poly_reg_model = LinearRegression()
    poly_reg_model.fit(poly_features, Y)

    return {'status': 'simple_polynominal',
            'coef': poly_reg_model.coef_.tolist(),
            'intercept': poly_reg_model.intercept_,
            'R square': poly_reg_model.score(X, Y)}


def multiple_linear_regression(request):
    indepVar = request.POST.getlist('listOfCheckboxes[]')
    depVar = request.POST.getlist('listOfRadio[]')

    # Load CSV and columns
    df = pd.read_csv('welcome/media/data.csv')
    X = df[[indepVar[0]]].to_numpy()
    Y = np.array((df[depVar[0]]))

    for column in indepVar[1:]:
        temp = df[[column]].to_numpy()
        X = np.concatenate([X, temp], axis=1)

    model = LinearRegression().fit(X, Y)
    
    return {'status': 'multiple_linear',
            'coef': model.coef_.tolist(),
            'intercept': model.intercept_,
            'R square': model.score(X, Y)}


def multiple_polynom_regression(request):
    indepVar = request.POST.getlist('listOfCheckboxes[]')
    depVar = request.POST.getlist('listOfRadio[]')
    
    df = pd.read_csv('welcome/media/data.csv')

    X = df[[indepVar[0]]].to_numpy()
    Y = np.array((df[depVar[0]]))

    for column in indepVar[1:]:
        temp = df[[column]].to_numpy()
        X = np.concatenate([X, temp], axis=1)

    poly = PolynomialFeatures(degree=int(request.POST['polynom_degree']),
                              include_bias=False)
    poly_features = poly.fit_transform(X)

    poly_reg_model = LinearRegression()
    poly_reg_model.fit(poly_features, Y)

    return {'status': 'multiple_polynom',
            'coef': poly_reg_model.coef_.tolist(),
            'intercept': poly_reg_model.intercept_,
            'R square': poly_reg_model.score(poly_features, Y)}