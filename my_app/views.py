from django.shortcuts import render

# Create your views here.
def Register(request):
    return render(request,'user_registration.html')

def Login(request):
    return render(request,'user_login.html') 

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def admin_new_worker_aprove(request):
    return render(request,'admin_new_worker_aprove.html')
    
def admin_users_details(request):
    return render(request,'admin_users_details.html')

def admin_user_profile_view(request):
    return render(request,'admin_user_profile_view.html')

def admin_worker_profile_view(request):
    return render(request,'admin_worker_profile_view.html')
    
def admin_workers_details(request):
    return render(request,'admin_workers_details.html')