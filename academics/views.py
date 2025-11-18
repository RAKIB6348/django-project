from django.shortcuts import render

# Create your views here.
def add_class(request):

    return render(request, 'class_acadmi/add_class.html')
