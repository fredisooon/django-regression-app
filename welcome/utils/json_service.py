from django.http import JsonResponse


def valid_response(regressionType):
    return JsonResponse({'error_flag': False,
                         'war_falg': False,
                         'message': 'OK',
                         'analysis_data': 'Valid',
                         'type_of_analys': regressionType})


def invalid_response(regressionType):
    return JsonResponse({'error_flag': False,
                            'war_falg': True,
                            'message': 'ERROR: Data type is not suitable for analysis',
                            'analysis_data': 'Invalid',
                            'type_of_analys': regressionType})


def logistic_result_response(model, indepVar):
    io_vars_dict = [
        {'name': 1,
         'input_vars': indepVar[0],
         'removed_vars': '-', 
         'method': 'Enter'}
    ]

    summary_dict = [
        {'name': 1,
         'pseudo_r_squared': model.prsquared,
         'log-Likelihood': model.llf,
         'll-null': model.llnull,
         'aic': model.aic,
         'bic': model.bic
         }
    ]

    coefs_dict = [
        {'name': '(Константа)', 'B': model.params[0], 'std_err': model.bse[0], 'beta': '-', 't-value': model.tvalues[0], 'p-value': model.pvalues[0]},
        {'name': indepVar[0], 'B': model.params[1], 'std_err': model.bse[1], 'beta': '-', 't-value': model.tvalues[1], 'p-value': model.pvalues[1]}
    ]

    return {
        'status': 'OK',
        'regression_type': 'simple_logistical',
        'io_vars': io_vars_dict,
        'summary': summary_dict,
        'coefs': coefs_dict
    }


def multiple_logistic_response(model, indepVar):
    io_vars_dict = [
        {'name': 1,
         'input_vars': indepVar,
         'removed_vars': '-', 
         'method': 'Enter'}
    ]

    summary_dict = [
        {'name': 1,
         'pseudo_r_squared': model.prsquared,
         'log-Likelihood': model.llf,
         'll-null': model.llnull,
         'aic': model.aic,
         'bic': model.bic
         }
    ]

    coefs_dict = [
        {'name': '(Константа)', 'B': model.params[0], 'std_err': model.bse[0], 'beta': '-', 't-value': model.tvalues[0], 'p-value': model.pvalues[0]}
    ]
    for i in range(len(indepVar)):
        temp_dict = {}
        temp_dict['name'] = indepVar[i]
        temp_dict['B'] = model.params[i+1]
        temp_dict['std_err'] = model.bse[i+1]
        temp_dict['beta'] = '-'
        temp_dict['t-value'] = model.tvalues[i+1]
        temp_dict['p-value'] = model.pvalues[i+1]
        coefs_dict.append(temp_dict)

    return {
        'status': 'OK',
        'regression_type': 'simple_logistical',
        'io_vars': io_vars_dict,
        'summary': summary_dict,
        'coefs': coefs_dict
    }


def valid_ordinal_response(regressionType, categoriesList):
    return JsonResponse({'error_flag': False,
                         'war_falg': False,
                         'message': 'OK',
                         'analysis_data': 'Valid',
                         'type_of_analys': regressionType,
                         'categories_list': categoriesList})