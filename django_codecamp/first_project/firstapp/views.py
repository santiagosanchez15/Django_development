from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm

# Create your views here.
def hello_world(request): #request sent by user
    '''Retrunes hello world when request is sent'''
    return HttpResponse("Hello world") # what you want to respond

class HelloEthiopia(View):

    def get(self, request):
        ''' when user sends request it returns Hello, Ethiopia'''
        return HttpResponse("Hello, Ethiopia")

def home(request):
    form = ReservationForm()

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Success")

    return render(request, 'index.html', {'form':form})