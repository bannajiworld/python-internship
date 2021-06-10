from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepageview(request):
    return render (request, 'home.html')

def aboutpageview(request):
    return render (request, 'about.html')

def contactpageview(request):
    return render (request, 'contact.html')

def myformpageview(request):
    return render (request, 'myform.html')

def process(request):
    print(request.method)
    print(request.POST)
    
    a= int(request.POST['txt1'])
    b= int(request.POST['txt2'])
    c= a+b
    print(c)

    return render(request, 'ans.html',{'f1':a,'f2':b,'mysum':c})