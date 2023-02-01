import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd


def linear_regression(request):
    
    indepVar = request.POST.getlist('listOfCheckboxes[]')
    depVar = request.POST.getlist('listOfRadio[]')

    # Load CSV and columns
    df = pd.read_csv('welcome/media/data.csv')

    X = np.array((df[indepVar[0]])).reshape((-1, 1))
    Y = np.array((df[depVar[0]]))

    model = LinearRegression().fit(X, Y)
    print(type(model))
    print
    return {'status': 'qvo',
            'coef': model.coef_.tolist(),
            'intercept': model.intercept_.tolist()}