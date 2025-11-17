from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.models import User

# Create your views here.
def dashboard_page(request):

    return render(request, 'dashboard.html')


#============== login page ===========================
def login_page(request):

    return render(request, 'login.html')


#==================== user login ======================
def user_login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        # Validation
        if not user_id or not password:
            messages.error(request, "User ID and Password are required.")
            return render(request, 'login.html')

        # user_id দিয়ে user খোঁজা
        try:
            user_obj = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            messages.error(request, "Invalid User ID or Password.")
            return render(request, 'login.html')

        # authenticate (username দিয়ে)
        user = authenticate(request, username=user_obj.username, password=password)

        if user is None:
            messages.error(request, "Invalid User ID or Password.")
            return render(request, 'login.html')

        # SUCCESS login
        login(request, user)

        # ===== Redirect based on user_type =====
        if user.user_type == 'Admin':
            return HttpResponse("This is a admin Panel")
        elif user.user_type == 'Teacher':
            return HttpResponse("This is a admin Panel")
        elif user.user_type == 'Student':
            return HttpResponse("This is a admin Panel")

        # fallback (যদি কিছু না মিলে)
        return redirect('login_page')

    # GET request
    return redirect('login_page')
