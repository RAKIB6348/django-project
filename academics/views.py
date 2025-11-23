from django.shortcuts import render, redirect
from academics.models import SchoolClass

# Create your views here.

#=============== add class =============================
def add_class(request):

    if request.method == 'POST':
        class_name = request.POST.get('class_name')
        class_code = request.POST.get('class_code')

        SchoolClass.objects.create(
            class_name = class_name,
            class_code = class_code,
        )

        return redirect('class_list')

    return render(request, 'academic/class/register.html')



#=============== list class ======================
def class_list(request):

    student_class = SchoolClass.objects.all()

    context = {
        'class_data' : student_class,
    }

    return render(request, 'academic/class/class_list.html', context)