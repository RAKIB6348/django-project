from django.shortcuts import render

# Create your views here.
def teacher_list(request):

    return render(request, 'teacher/teacher_list.html')



def add_teacher(request):

    return render(request, 'teacher/add_teacher.html')