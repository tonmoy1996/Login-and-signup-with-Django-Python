from django.shortcuts import render

from django.http import HttpResponse 

from Login.form import LoginForm	

# Create your views here.


def index(request):

	'''data={'name':"EnterName"
	     }'''
	
	return render(request,'index.html')


def home(request):
	'''return HttpResponse("<h1>Welcome Home!!</h1>")	'''
	'''return render(request,'home.html')'''

	lo=LoginForm()

	return render(request,'home.html',{'form':lo})