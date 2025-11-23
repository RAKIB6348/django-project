from django.shortcuts import render, redirect
from academics.models import *


def add_subject_page(request):
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        subject_code = request.POST.get('subject_code')

        Subject.objects.create(
                subject_name = subject_name,
                subject_code = subject_code,
            )

        return redirect('list_subject_page')

    return render(request, 'academic/subject/register.html')


def list_subject_page(request):

    subject = Subject.objects.all()

    context = {
        'subject' : subject,
    }

    return render(request, 'academic/subject/list.html', context)