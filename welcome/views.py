from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from welcome.forms import UploadFileForm
from welcome.utils.uploadings import get_list_of_file_headers

# Create your views here.

def landing(request):
    return render(request, "welcome/landing.html")

def workspace(request):
    if request.method == 'POST':
        print('SECONT AJAX REQUEST GOING THROUGHT $THIS VIEW')
        print(request.POST)
        form = UploadFileForm(request.POST, request.FILES)
        print(request.FILES['file'])
        if form.is_valid():
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
    list1 = request.POST.getlist('listOfRadio[]')
    list2 = request.POST.getlist('listOfCheckboxes[]')

    if (len(list1) == 1):
        if (len(list2) == 1):
            return JsonResponse({'error_flag': False,
                                 'war_falg': False,
                                 'message': 'OK',
                                 'analysis_data': 'Valid',
                                 'type_of_analys': 'Simple Linear'})
        elif (len(list2) > 1):
            return JsonResponse({'error_flag': False,
                                 'war_falg': False,
                                 'message': 'OK',
                                 'analysis_data': 'Valid',
                                 'type_of_analys': 'Multiple Linear'})
        elif (len(list2) == 0):
            return JsonResponse({'error_flag': False,
                                 'war_falg': True,
                                 'message': 'WAR: Independent variables are not selected'})
    elif (len(list1) == 0 ):
        return JsonResponse({'error_flag': False,
                             'war_falg': True,
                            'message': 'WAR: Dependent variable not selected'})    
    else:
        return JsonResponse({'error_flag': True,
                             'war_falg': False,
                             'message': 'ERROR: There can be only one dependent variable'})    