from django.shortcuts import render


def view_profile_page(request):

    user = request.user

    return render(request, 'profile/profile.html', {'user':user})