from django.shortcuts import render

# Create your views here.
def add_student(request):

    return render(request, 'student/add_student.html')



# student_list
def student_list(request):

    return render(request, 'student/student_list.html')