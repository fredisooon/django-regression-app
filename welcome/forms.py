from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'accept': ".csv"}))
    file.label = "Выберите файл"
    
    