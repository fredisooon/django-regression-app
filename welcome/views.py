from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from welcome.forms import UploadFileForm
from welcome.utils.uploadings import get_list_of_file_headers

# Create your views here.

def landing(request):
    return render(request, "welcome/landing.html")

def workspace(request):
    if request.method == 'POST':
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