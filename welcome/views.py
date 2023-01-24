from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from welcome.forms import UploadFileForm
from welcome.utils.uploadings import handle_uploaded_file

# Create your views here.

def landing(request):
    return render(request, "welcome/landing.html")

def workspace(request):
    if request.method == 'POST':
       form = UploadFileForm(request.POST, request.FILES)
       print(request.FILES['file'])
       if form.is_valid():
            f = request.FILES['file']
            handle_uploaded_file(f)
            return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
       else:
           return JsonResponse({'error': True, 'errors': form.errors})
    else:
        form = UploadFileForm()
        return render(request, 'welcome/upload-workspace.html', {'form': form})