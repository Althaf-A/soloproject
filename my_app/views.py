from django.shortcuts import redirect, render
import random
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth, User
from my_app.models import *
from datetime import datetime
from webscraping.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
# Create your views here.
def Register(request):
   if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        contact = request.POST['contact']
        city = request.POST['city']
        photo = request.FILES['photo']
        username = email
        password = random.randint(10000, 99999)
        dept = request.POST['dept']
        if user_register.objects.filter(email=email).exists():
         msg_warning = "Mail id exists"
         return render(request,'user_registration.html',{'msg_warning':msg_warning})
        else:
         register = user_register(fullname=fname, email=email, contact_no=contact,photo=photo,city=city,
                              username=username, password=password, category_id=dept, regdate=datetime.now())
         register.save()  
         messages.success(
         request, 'username and password for exam is sent to your registered mail id.........')
         member = user_register.objects.get(id=register.id)
         subject = 'Greetings from wiflix project'
         message = 'Congratulations,\n' \
            'You have successfully registered with .\n' \
            'username :'+str(member.username)+'\n' 'password :'+str(member.password) + \
            '\n' 'ALL THE BEST WISHES FOR Using This Site ' + \
            '\n' 'Login to test :http://127.0.0.1:8000/'
         recepient = str(email)
         send_mail(subject, message, EMAIL_HOST_USER,
                  [recepient], fail_silently=False)
         msg_success = "Registration completed Check Your Mail"
        return render(request,'user_registration.html',{'msg_success':msg_success})              
   else:
      vars1 = category.objects.all()
      return render(request, 'user_registration.html', {'vars1': vars1})
  

def Login(request):

    des = category.objects.get(name='user')
    des1 = category.objects.get(name='worker')
    des2 = category.objects.get(name='contractor')
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        if user_register.objects.filter(email=email, password=password, category_id=des.id).exists():
            member = user_register.objects.get(
                email=request.POST['username'], password=request.POST['password'])
            request.session['username'] = member.category_id
            request.session['username1'] = member.fullname
            request.session['username2'] = member.id
            z = user_register.objects.filter(id=member.id)
            return render(request, 'user_dashboard.html', {'member': member,'z':z})
        elif user_register.objects.filter(email=email, password=password, category_id=des1.id).exists():
            member = user_register.objects.get(
                email=request.POST['username'], password=request.POST['password'])
            request.session['usernamew'] = member.category_id
            request.session['usernamew1'] = member.fullname
            request.session['usernamew2'] = member.id
            return render(request, 'worker_dashboard.html', {'member': member})
        elif user_register.objects.filter(email=email, password=password, category_id=des2.id).exists():
            member = user_register.objects.get(
                email=request.POST['username'], password=request.POST['password'])
            request.session['usernamec'] = member.category_id
            request.session['usernamec1'] = member.fullname
            request.session['usernamec2'] = member.id
            return render(request, 'worker_dashboard.html', {'member': member})

        elif request.method == 'POST':
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            user = authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
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
    if 'username2' in request.session:

        if request.session.has_key('username2'):
            username2 = request.session['username2']

        z = user_register.objects.filter(id=username2)

        return render(request,'user_dashboard.html', {'z': z})
    else:
        return redirect('/')

def user_search_worker(request):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('username2'):
            username2 = request.session['username2']

        z = user_register.objects.filter(id=username2)

        return render(request,'user_search_worker.html',{'z': z})
    else:
        return redirect('/')

    
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
    if 'usernametw2' in request.session:

        if request.session.has_key('usernamew2'):
            usernamew2 = request.session['usernamew2']

        z = user_register.objects.filter(id=usernamew2)

        return render(request,'worker_dashboard.html', {'z': z})
    else:
        return redirect('/')


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

def worker_work_status_cards(request):
    return render(request,'worker_work_status_cards.html')

def worker_curent_work(request):
    return render(request,'worker_curent_work.html')
    
def worker_completed_workes(request):
    return render(request,'worker_completed_workes.html')

def worker_curent_ongoingworks(request):
    return render(request,'worker_curent_ongoingworks.html')

def worker_curent_addwork(request):
    return render(request,'worker_curent_addwork.html')