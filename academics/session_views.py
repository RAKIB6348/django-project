from django.shortcuts import render


def add_session(request):

    return render(request, 'academic/session/add_session.html')



def session_list(request):

    return render(request, 'academic/session/list.html')