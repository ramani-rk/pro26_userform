from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def userform(request):

    return render(request,'userform.html')