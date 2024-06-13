# Create your views here.
from django.shortcuts import render

# render home page
def home(request):
    # return render(request, 'ibm-home.html')
    return render(request, 'cosmos-home.html')