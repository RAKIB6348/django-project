from django.shortcuts import render, redirect



def add_section(request):

    return render(request, 'academic/section/register_section.html')