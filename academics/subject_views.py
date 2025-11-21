from django.shortcuts import render


def add_subject_page(request):

    return render(request, 'academic/subject/register.html')


def list_subject_page(request):

    return render(request, 'academic/subject/list.html')