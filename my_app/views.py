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
    
def admin_user_activity(request):
    return render(request,'admin_user_activity.html')

def admin_workers_register(request):
    return render(request,'admin_workers_register.html')

def admin_feedback_cards(request):
    return render(request,'admin_feedback_cards.html')

def admin_workers_feedbacks(request):
    return render(request,'admin_workers_feedbacks.html')

def admin_users_feedbacks(request):
    return render(request,'admin_users_feedbacks.html')

############################user################################

def user_dashboard(request):
    return render(request,'user_dashboard.html')

def user_search_worker(request):
    return render(request,'user_search_worker.html')

def user_worker_profile(request):
    return render(request,'user_worker_profile.html')

def user_worker_reports(request):
    return render(request,'user_worker_reports.html')

def user_history_list(request):
    return render(request,'user_history_list.html')