from django.shortcuts import render

# Create your views here.

def retrieve(request): 
    '''Retrieve path to html file'''
    return render(request, "Index.html")