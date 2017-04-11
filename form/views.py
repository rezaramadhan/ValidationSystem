from django.shortcuts import render

# Create your views here.

def validation_form(request):
    return render(request, 'form/validation_form.html', {})
