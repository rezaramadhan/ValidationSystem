from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from validate import validate_email
import json

# Create your views here.
@csrf_exempt
def validation_form(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    email = body["email"]
    result = validate_email(email)
    response = "{ valid : '" + str(True) + "' }"
    return HttpResponse(response)
