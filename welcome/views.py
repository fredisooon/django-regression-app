from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from welcome.forms import UploadFileForm
from welcome.utils.file_utils import *
from welcome.utils.validate_service import *
from django.conf import settings
import pandas as pd

# Create your views here.

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
    
    # проверка валидности данных для применения Простой Линейной Регрессии
    if (len(depVar) == 1 and len(indepVar) == 1):
        if (set_of_var_is_numeric(depVar, indepVar)):
            return JsonResponse({'error_flag': False,
                                 'war_falg': False,
                                  'message': 'OK',
                                  'analysis_data': 'Valid',
                                  'type_of_analys': 'Простая Линейная'})
        else:
            return JsonResponse({'error_flag': False,
                                 'war_falg': True,
                                 'message': 'ERROR: Data type is not suitable for analysis',
                                 'analysis_data': 'Invalid',
                                 'type_of_analys': 'Простая Линейная'})
    
    
    # проверка валидности данных для применения 
    # Множественной или Полиноминальной регрессий
    if (len(depVar) == 1 and len(indepVar) > 1):
        if (set_of_var_is_numeric(depVar, indepVar)):
            return JsonResponse({'error_flag': False,
                                 'war_falg': False,
                                 'message': 'OK',
                                 'analysis_data': 'Valid',
                                 'type_of_analys': ['Мульти Линейная', 'Полиноминальная']})
        else:
            return JsonResponse({'error_flag': False,
                                 'war_falg': True,
                                  'message': 'ERROR: Data type is not suitable for analysis',
                                  'analysis_data': 'Invalid',
                                  'type_of_analys': ['Мульти Линейная', 'Полиноминальная']})
