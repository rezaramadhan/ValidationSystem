from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from validate import validate_email
import json
import re
# Create your views here.
@csrf_exempt
def validation_form(request):
    j = request.body.decode('utf-8')
    j = re.sub(r"{\s*(\w)", r'{"\1', j)
    j = re.sub(r",\s*(\w)", r',"\1', j)
    j = re.sub(r"(\w):", r'\1":', j)
    body = json.loads(j)
    email = body["email"]
    result = validate_email(email)
    response = "{ valid : '" + str(result) + "' }"
    return HttpResponse(response)
