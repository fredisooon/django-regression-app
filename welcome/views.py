from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from welcome.forms import UploadFileForm
from welcome.utils.file_utils import *
from welcome.utils.validate_service import *
from welcome.utils.regression_service import *
from welcome.utils.json_service import *

# Create your views here.

def analysis(request):
    print("INSIDE ANALYSIS METHOD")
    print(request.POST['analysis_type'])

    if (request.POST['analysis_type'] == 'simple_linear'):
        return JsonResponse(simple_linear_regression(request))
    elif (request.POST['analysis_type'] == 'simple_polynominal'):
        return JsonResponse(simple_polynominal_regression(request))
    elif (request.POST['analysis_type'] == 'multiple_linear'):
        return JsonResponse(multiple_linear_regression(request))
    elif (request.POST['analysis_type'] == 'multiple_polynominal'):
        return JsonResponse(multiple_polynom_regression(request))
    elif (request.POST['analysis_type'] == 'simple_logistic'):
        return JsonResponse(simple_logistic_regression(request))
    elif (request.POST['analysis_type'] == 'multiple_logistic'):
        return JsonResponse(multiple_logistic_regression(request))


    return JsonResponse({'status': 'error',
                         'message': 'no regression is selected'}) 


def landing(request):
    return render(request, "welcome/landing.html")


def workspace(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            save_file_to_media(request.FILES['file'])
            headersList = get_list_of_file_headers(request.FILES)
            if headersList:
                return JsonResponse({'error': False,
                                    'message': 'File uploaded Successfully',
                                    'empty_flag': False,
                                    'headers_list': headersList})
            else:
                return JsonResponse({'error': False,
                                    'message': 'File uploaded Successfully',
                                    'empty_flag': True})
        else:
           return JsonResponse({'error': True,
                                'errors': form.errors})
    else:
        form = UploadFileForm()
        return render(request, 'welcome/upload-workspace.html', {'form': form})


def result(request):
    depVar = request.POST.getlist('listOfRadio[]')
    indepVar = request.POST.getlist('listOfCheckboxes[]')
    


    # обработка невалидных наборов переменных
    if (len(depVar) == 0 and len(indepVar) == 0):
        return JsonResponse({'error_flag': False,
                             'war_falg': True,
                             'message': 'WAR: Dependent and Independed variables not selected'})
    elif (len(depVar) == 0 and len(indepVar) == 1):
        return JsonResponse({'error_flag': False,
                             'war_falg': True,
                             'message': 'WAR: Dependent variable not selected'})
    elif (len(depVar) == 1 and len(indepVar) == 0):
        return JsonResponse({'error_flag': False,
                             'war_falg': True,
                             'message': 'WAR: Independent variables are not selected'})
    elif (len(depVar) != 0 and len(depVar) != 1):
        return JsonResponse({'error_flag': True,
                             'war_falg': True,
                             'message': 'Error: Error in the number of dependent variables'})
    

# проверка данных на парность (одна зависимая, одна независимая переменные)
    if (is_pair_regression_dataset(depVar, indepVar)):
        print('Dataset is Pair')

        if (is_logistic_dataset(depVar, indepVar)):
            print('Dataset is Logistic')
            return valid_response(['Простая Логистическая'])

        elif (is_ordinal_dataset(depVar, indepVar)):
            print('Dataset is Ordinal')
            return valid_response(['Простая Порядковая'])

        elif (is_linear_dataset(depVar, indepVar)):
            print('Dataset is Linear')
            return valid_response(['Простая Линейная', 'Простая Полиноминальная'])
        
        else:
            return invalid_response(['Простая Линейная', 'Простая Полиноминальная'])

# проверка данных на множественность (одна зависимая, n независимых переменных)
    elif (is_multiple_regression_dataset(depVar, indepVar)):
        print('Dataset is Multiple')
        
        if (is_multiple_logistic_dataset(depVar, indepVar)):
            print('Dataset is Multiple Logistic')
            return valid_response(['Множественная Логистическая'])

        elif (is_multiple_ordinal_dataset(depVar, indepVar)):
            print('Dataset is Multiple Ordinal')
            return valid_response(['Множественная Порядковая'])

        elif (is_multiple_linear_dataset(depVar, indepVar)):
            print('Dataset is Multiple Linear')
            return valid_response(['Множественная Линейная', 'Множественная Полиноминальная'])

        else:
            return invalid_response(['Множественная Линейная', 'Множественная Полиноминальная'])
            
    else:
        print("Something went wrong :|")