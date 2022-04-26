from django.shortcuts import redirect, render
import random
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth, User
from my_app.models import *
from datetime import datetime
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
# Create your views here.
def Register(request):
   if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        contact = request.POST['contact']
        username = email
        password = random.randint(10000, 99999)
        dept = request.POST['dept']
        if candidates.objects.filter(email=email).exists():
         msg_warning = "Mail id exists"
         return render(request,'user_registration.html',{'msg_warning':msg_warning})
        else:
         register = candidates(fullname=fname, email=email, contact_no=contact,
                              username=username, password=password, deptmnt_id=dept, regdate=datetime.now())
         register.save()                
   else:
      vars1 = department.objects.all()
      return render(request, 'user_registration.html', {'vars1': vars1})
   return render(request, 'user_registration.html')

def Login(request):

    des = department.objects.get(name='user')
    des1 = department.objects.get(name='worker')
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        if candidates.objects.filter(email=email, password=password, deptmnt_id=des.id).exists():
            member = candidates.objects.get(
                email=request.POST['username'], password=request.POST['password'])
            request.session['usernametm'] = member.deptmnt_id
            request.session['usernametm1'] = member.fullname
            request.session['usernametm2'] = member.id
            #request.session['usernamehr2'] = member.branch
            return render(request, 'user_dashboard.html', {'member': member})
        elif candidates.objects.filter(email=email, password=password, deptmnt_id=des1.id).exists():
            member = candidates.objects.get(
                email=request.POST['username'], password=request.POST['password'])
            request.session['usernametm'] = member.deptmnt_id
            request.session['usernametm1'] = member.fullname
            request.session['usernametm2'] = member.id
            #request.session['usernamehr2'] = member.branch
            return render(request, 'worker_dashboard.html', {'member': member})

        elif request.method == 'POST':
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                  context = {'msg_error': 'Invalid data'}
                  return render(request, 'user_login.html',context)
    
    return render(request, 'user_login.html')  

def logout(request):
    auth.logout(request)
    return redirect("/") 
    
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

def admin_all_workers(request):
    return render(request,'admin_all_workers.html')

def admin_all_contractors(request):
    return render(request,'admin_all_contractors.html')


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

def user_post_feedback(request):
    return render(request,'user_post_feedback.html')


    ######################worker##########
    
def worker_dashboard(request):
    return render(request,'worker_dashboard.html')

def worker_work_details_cards(request):
    return render(request,'worker_work_details_cards.html')

def worker_post_work_details(request):
    return render(request,'worker_post_work_details.html')

def worker_view_edit_details(request):
    return render(request,'worker_view_edit_details.html')

def worker_edit_work_details(request):
    return render(request,'worker_edit_work_details.html')

def worker_user_enquiry_list(request):
    return render(request,'worker_user_enquiry_list.html')

def worker_history_list(request):
    return render(request,'worker_history_list.html')

def worker_feedback_cards(request):
    return render(request,'worker_feedback_cards.html')

def worker_post_feedback(request):
    return render(request,'worker_post_feedback.html')

def worker_view_feedback(request):
    return render(request,'worker_view_feedback.html')