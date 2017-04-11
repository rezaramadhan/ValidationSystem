from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def validation_form(request):
     return render(request, 'form/validation_form.html', {})

