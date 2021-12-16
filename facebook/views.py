from django.shortcuts import render,HttpResponse

# Create your views here.
def face(request):
    return render(request,'face.html')
