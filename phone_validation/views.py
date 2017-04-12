from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
from random import randint

phoneDict = []

# Create your views here.	
@csrf_exempt
def validation_form(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(request.body)
	to = body["phone"] #6281218641998

	api_key = '9c085211'
	api_secret = '77a3426d684c3cbd'
	verificationCode = randint(1000, 9999)
	phoneDict[to] = verificationCode

	url = 'https://rest.nexmo.com/sms/json?api_key=' + api_key + '&api_secret=' + api_secret + '&to=' + to + '&from=NexmoWorks&text=' + verificationCode

	print(url)
	r = requests.get(url)

	print(r.text)

	return HttpResponse('{status : "OK"}')

@csrf_exempt
def code_verification(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(request.body)
	phone = body["phone"] #6281218641998
	verificationCode = body["phone"]

	if(phoneDict[phone] == verificationCode):
		return HttpResponse('{valid : "yes"}')
	else:
		return HttpResponse('{valid : "no"}')