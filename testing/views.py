from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from testing.utils.uploadings import handle_uploaded_file
from .forms import UploadFileForm


def hello(request):
    if request.method == 'POST':
        response = "File " + request.FILES['file'].name
        return HttpResponse(response)
        


def index(request):
    if request.method == 'POST':
       form = UploadFileForm(request.POST, request.FILES)
       if form.is_valid():
            #string = "File " + request.FILES['file'].name
            #return JsonResponse(string)
            f = request.FILES['file']
            handle_uploaded_file(f)
            return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
       else:
           return JsonResponse({'error': True, 'errors': form.errors})
    else:
        form = UploadFileForm()
        return render(request, 'index.html', {'form': form})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/testing/upload')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})