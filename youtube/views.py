from django.shortcuts import render,HttpResponse

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def home(request):
    return HttpResponse('welcome to the HOME page')
def hello(request):
    msg='this page from context'
    return render(request,'hello.html',context={'a':msg})
