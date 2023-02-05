import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import statsmodels.api as sm
import json


def simple_linear_regression(request):
    
    indepVar = request.POST.getlist('listOfCheckboxes[]')
    depVar = request.POST.getlist('listOfRadio[]')

    df = pd.read_csv('welcome/media/data.csv')

    X = np.array((df[indepVar[0]])).reshape((-1, 1))
    Y = np.array((df[depVar[0]]))
    X = sm.add_constant(X)

    est_model=sm.OLS(Y, X).fit()

    io_vars_dict = [
        {'name': 1, 'input_vars': indepVar[0], 'removed_vars': '-', 'method': 'Enter'}
    ]

    summary_dict = [
        {'name': 1, 'R': est_model.rsquared ** 0.5, 'R_squared': est_model.rsquared, 'R_adj': est_model.rsquared_adj, 'std_err_est': est_model.scale ** 0.5}
    ]

    anova_dict = [
        {'name': 'Регрессия', 'sum_of_square': '-', 'deg_freedom': est_model.df_model, 'square_mean': '-', 'f-value': est_model.fvalue, 'p-value': '-'},
        {'name': 'Остаток', 'sum_of_square': '-', 'deg_freedom': '-', 'square_mean': '-', 'f-value': '-', 'p-value': '-'},
        {'name': 'Всего', 'sum_of_square': '-', 'deg_freedom': '-', 'square_mean': '-', 'f-value': '', 'p-value': '-'}
    ]

    coefs_dict = [
        {'name': '(Константа)', 'B': est_model.params[0], 'std_err': est_model.bse[0], 'beta': '-', 't-value': est_model.tvalues[0], 'p-value': est_model.pvalues[0]},
        {'name': indepVar[0], 'B': est_model.params[1], 'std_err': est_model.bse[1], 'beta': '-', 't-value': est_model.tvalues[1], 'p-value': est_model.pvalues[1]}
    ]

    return {
        'status': 'OK',
        'regression_type': 'simple_linear',
        'io_vars': io_vars_dict,
        'summary': summary_dict,
        'anova': anova_dict,
        'coefs': coefs_dict
    }


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
            'R square': poly_reg_model.score(poly_features, Y)}


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

    X = sm.add_constant(X) 
    est_model=sm.OLS(Y, X).fit()

    print(est_model.summary())

    io_vars_dict = [
        {'name': 1, 'input_vars': indepVar, 'removed_vars': '-', 'method': 'Enter'}
    ]

    summary_dict = [
        {'name': 1, 'R': est_model.rsquared ** 0.5, 'R_squared': est_model.rsquared, 'R_adj': est_model.rsquared_adj, 'std_err_est': est_model.scale ** 0.5}
    ]

    anova_dict = [
        {'name': 'Регрессия', 'sum_of_square': '-', 'deg_freedom': est_model.df_model, 'square_mean': '-', 'f-value': est_model.fvalue, 'p-value': '-'},
        {'name': 'Остаток', 'sum_of_square': '-', 'deg_freedom': '-', 'square_mean': '-', 'f-value': '-', 'p-value': '-'},
        {'name': 'Всего', 'sum_of_square': '-', 'deg_freedom': '-', 'square_mean': '-', 'f-value': '', 'p-value': '-'}
    ]

    coefs_dict = [
        {'name': '(Константа)', 'B': est_model.params[0], 'std_err': est_model.bse[0], 'beta': '-', 't-value': est_model.tvalues[0], 'p-value': est_model.pvalues[0]}
    ]
    
    for i in range(len(indepVar)):
        temp_dict = {}
        temp_dict['name'] = indepVar[i]
        temp_dict['B'] = est_model.params[i+1]
        temp_dict['std_err'] = est_model.bse[i+1]
        temp_dict['beta'] = '-'
        temp_dict['t-value'] = est_model.tvalues[i+1]
        temp_dict['p-value'] = est_model.pvalues[i+1]
        coefs_dict.append(temp_dict)

        
    return {
        'status': 'OK',
        'regression_type': 'multiple_linear',
        'io_vars': io_vars_dict,
        'summary': summary_dict,
        'anova': anova_dict,
        'coefs': coefs_dict
    }


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