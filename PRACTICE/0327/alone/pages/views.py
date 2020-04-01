from django.shortcuts import render

# Create your views here.
def home(request,name):
    context = {
        'name' : name
    }
    return render(request,'home.html',context)

def community(request,name):
    context = {
        'name' : name
    }
    return render(request,'community.html',context)