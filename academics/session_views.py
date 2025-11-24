from django.shortcuts import render, redirect
from academics.models import Session


def add_session(request):

    if request.method == 'POST':
        session_name = request.POST.get('session_name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        Session.objects.create(
            session_name = session_name,
            start_date = start_date,
            end_date = end_date,
        )

        return redirect('session_list')

    return render(request, 'academic/session/add_session.html')



def session_list(request):

    session = Session.objects.all()

    context = {
        'session' : session,
    }

    return render(request, 'academic/session/list.html', context)