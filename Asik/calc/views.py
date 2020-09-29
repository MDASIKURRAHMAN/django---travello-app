from django.shortcuts import render
from django .http import HttpResponse

'''
#for printing hello world
def home(request):
    return HttpResponse ("Hello world")
'''
'''
#for printing hello world with html page
def home(request):
    return render (request,"home.html")

'''
'''
#for printing  with html page and jinja code
def home(request):
    return render (request,"home.html",{'name':'asik'})
'''

def home(request):
    return render (request,"home.html")

'''
# using get method
def add(request):
        val1 = int (request.GET.get('num1'))
        val2 = int (request.GET.get('num2'))
        res = val1+val2
        return render(request,"result.html",{'result':res})
'''
#using post method
def add(request):
        val1 = int (request.POST['num1'])
        val2 = int (request.POST['num2'])
        res = val1+val2
        return render(request,"result.html",{'result':res})


     

    



# Create your views here.
