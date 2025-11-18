from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import User
from accounts.admin_models import AdminProfile
from django.contrib.auth.decorators import login_required



#============== admin register ========================

def register_admin(request):
    # POST request এ form submit করলে data আসবে
    if request.method == 'POST':

        # form theke data collect
        username          = request.POST.get('username')
        email             = request.POST.get('email')
        password          = request.POST.get('password')
        confirm_password  = request.POST.get('confirm_password')

        first_name        = request.POST.get('first_name')
        last_name         = request.POST.get('last_name')
        phone             = request.POST.get('phone')
        gender            = request.POST.get('gender')
        country           = request.POST.get('country') or "Bangladesh"
        city              = request.POST.get('city')
        zip_code          = request.POST.get('zip_code')

        profile_pic       = request.FILES.get('profile_pic')

        # basic validation: password match check
        if password != confirm_password:
            messages.error(request, "Password and Confirm Password do not match.")
            return render(request, 'admin/register.html')

        # basic validation: must have username & email
        if not username or not email:
            messages.error(request, "Username and Email are required.")
            return render(request, 'admin/register.html')

        # ---- USER CREATE ----
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            user_type='Admin',   
        )

        # extra user info set
        user.first_name = first_name
        user.last_name  = last_name
        user.save()  

        # ---- ADMIN PROFILE CREATE ----
        AdminProfile.objects.create(
            user=user,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            gender=gender,
            city=city,
            zip_code=zip_code,
            country=country,
            profile_pic=profile_pic,
            password=password,
            confirm_password=confirm_password,
        )
        

        messages.success(request, "Admin registered successfully!")
        return render(request, 'admin/register.html') 

    return render(request, 'admin/register.html')




#======================== admin home dash ==========================
@login_required
def admin_dashboard(request):

    return render(request, 'admin/home.html')