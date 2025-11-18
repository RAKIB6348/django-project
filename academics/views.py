from django.shortcuts import render

# Create your views here.

#=============== add class =============================
def add_class(request):

    return render(request, 'academic/class/register.html')



#=============== list class ======================
def class_list(request):

    return render(request, 'academic/class/class_list.html')