from django.shortcuts import redirect, render
import random
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth, User
from numpy import var
from my_app.models import *
from datetime import datetime
from webscraping.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlencode
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
 
    
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        des = category.objects.get(name='user')
        des1 = category.objects.get(name='worker')
        des2 = category.objects.get(name='contractor')
        if user_register.objects.filter(email=email, password=password, category_id=des.id).exists():
            member = user_register.objects.get(
                email=request.POST['username'], password=request.POST['password'])
            request.session['username'] = member.category_id
            request.session['username1'] = member.fullname
            request.session['username2'] = member.id
            z = user_register.objects.filter(id=member.id)
            return render(request, 'user_dashboard.html', {'member': member,'z':z})
        elif user_register.objects.filter(email=email, password=password, category_id=des1.id ,status=1).exists():
            member = user_register.objects.get(
                email=request.POST['username'], password=request.POST['password'])
            request.session['usernamew'] = member.category_id
            request.session['usernamew1'] = member.fullname
            request.session['usernamew2'] = member.id
            z = user_register.objects.filter(id=member.id)
            return render(request, 'worker_dashboard.html', {'member': member,'z':z})
        elif user_register.objects.filter(email=email, password=password, category_id=des2.id ,status=1).exists():
            member = user_register.objects.get(
                email=request.POST['username'], password=request.POST['password'])
            request.session['usernamew'] = member.category_id
            request.session['usernamew1'] = member.fullname
            request.session['usernamew2'] = member.id
            z = user_register.objects.filter(id=member.id)
            return render(request, 'worker_dashboard.html', {'member': member,'z':z})

        elif request.method == 'POST':
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            user = authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                request.session['SAdm_id'] = user.id
                
                return redirect('admin_dashboard')
            else:
                  context = {'msg_error': 'Invalid data'}
                  return render(request, 'user_login.html',context)
    
    return render(request, 'user_login.html')  

def logout(request):
    auth.logout(request)
    return redirect("/") 
    
def admin_dashboard(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        ur = category.objects.get(name='user')
        uss= user_register.objects.filter(category_id=ur.id).count()
        wr = category.objects.get(name='worker')
        wrkr= user_register.objects.filter(category_id=wr.id).count()
        co = category.objects.get(name='user')
        con= user_register.objects.filter(category_id=co.id).count()
        return render(request, 'admin_dashboard.html', {'users': users,'uss':uss,'wrkr':wrkr,'con':con})
    else:
        return redirect('/')

def admin_new_worker_aprove(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        wrkr = category.objects.get(name='user')
        wr= user_register.objects.filter(status=0).exclude(category_id=wrkr.id)
        if request.method == 'POST':
            id = request.GET.get('tid')
            v = user_register.objects.get(id=id)
            v.status = 1
            v.save()
        return render(request,'admin_new_worker_aprove.html',{'users': users,'wr':wr})
    else:
        return redirect('/')

def reject_worker(request):
    if request.method == 'POST':
        id = request.GET.get('tid')            
        v = user_register.objects.get(id=id)
        v.status=2
        v.save()
    return redirect('admin_new_worker_aprove')

def admin_worker_status_cards(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        ur = category.objects.get(name='user')
        return render(request,'admin_worker_status_cards.html',{'users': users})
    else:
        return redirect('/')

def admin_aproved_workers(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        wrkr = category.objects.get(name='user')
        wr= user_register.objects.filter(status=1).exclude(category_id=wrkr.id)
        if request.method == 'POST':
            id = request.GET.get('tid')
            v = user_register.objects.get(id=id)
            v.status = 2
            v.save()
        return render(request,'admin_aproved_workers.html',{'users': users,'wr':wr})
    else:
        return redirect('/')

def admin_rejected_workers(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        wrkr = category.objects.get(name='user')
        wr= user_register.objects.filter(status=2).exclude(category_id=wrkr.id)
        
        if request.method == 'POST':
            id = request.GET.get('tid')
            
            v = user_register.objects.get(id=id)
            v.status=1
            v.save()
            print(v)
        return render(request,'admin_rejected_workers.html',{'users': users,'wr':wr})
    else:
        return redirect('/')

def admin_users_details(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr = category.objects.get(name='user')
        ur= user_register.objects.filter(category_id=usr.id)
        return render(request,'admin_users_details.html',{'users': users,'ur':ur})
    else:
        return redirect('/')

def admin_user_profile_view(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        mem= user_register.objects.get(id=id)

        return render(request,'admin_user_profile_view.html',{'users': users,'mem':mem})
    else:
        return redirect('/')

def admin_worker_profile_view(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        mem= user_register.objects.get(id=id)
        # wr=work_details.objects.get(worker_id=mem)

        return render(request,'admin_worker_profile_view.html',{'users': users,'mem':mem})
    else:
        return redirect('/')

    
def admin_workers_details(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        des= category.objects.get(name='user')
        mem= category.objects.filter().exclude(name='user')
        mem1=user_register.objects.filter().exclude(category_id=des.id).values('work_name').distinct()

        return render(request,'admin_workers_details.html',{'users': users,'mem':mem,'mem1':mem1})
    else:
        return redirect('/')

@csrf_exempt
def admin_all_workers_table(request):
    if 'SAdm_id' in request.session:
        dept = request.POST['depmt']
        desi = request.POST['desi']
        names = user_register.objects.filter( category_id=dept, work_name=desi).values(
            'category__name', 'city',  'fullname', 'work_name', 'id')
        print(dept)
        print(desi)
        print(names)
        print('hai')
        return render(request,'admin_all_workers_table.html',{'names': names})
    else:
        return redirect('/')

def admin_user_activity(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        ur= feedback.objects.filter(user_id__id=id)

        return render(request,'admin_user_activity.html',{'users': users,'ur':ur})
    else:
        return redirect('/')

def admin_workers_register(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        ur= feedback.objects.filter(worker_id__id=id)

        return render(request,'admin_workers_register.html',{'users': users,'ur':ur})
    else:
        return redirect('/')

def admin_feedback_cards(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)

        return render(request,'admin_feedback_cards.html',{'users': users})
    else:
        return redirect('/')

def admin_workers_feedbacks(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        mem= feedback.objects.filter(replay_status=0)

        return render(request,'admin_workers_feedbacks.html',{'users': users,'mem':mem})
    else:
        return redirect('/')

def admin_users_feedbacks(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        mem= feedback.objects.filter(replay_status=1)

        return render(request,'admin_users_feedbacks.html',{'users': users,'mem':mem})
    else:
        return redirect('/')

def admin_all_workers(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        wrkr = category.objects.get(name='worker')
        wr= user_register.objects.filter(category_id=wrkr.id)
        return render(request,'admin_all_workers.html',{'users': users,'wr':wr})
    else:
        return redirect('/')


def admin_all_contractors(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        cokr = category.objects.get(name='contractor')
        co= user_register.objects.filter(category_id=cokr.id)
        return render(request,'admin_all_contractors.html',{'users': users,'co':co})
    else:
        return redirect('/')


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
    if 'username2' in request.session:
        if request.session.has_key('username2'):
            username2 = request.session['username2']
        z = user_register.objects.filter(id=username2)
        des= category.objects.get(name='user')
        mem= category.objects.filter().exclude(name='user')
        mem1=user_register.objects.filter().exclude(category_id=des.id).values('work_name').distinct()
        m3=user_register.objects.filter().exclude(category_id=des.id).values('city').distinct()
        return render(request,'user_search_worker.html',{'mem':mem,'z': z,'mem1':mem1,'m3':m3})
    else:
        return redirect('/')

@csrf_exempt
def user_search_worker_table(request):
    if 'username2' in request.session:
        workt = request.POST['workt']
        workn = request.POST['workn']
        citty = request.POST['city']

        names = user_register.objects.filter(city=citty, category_id=workt, work_name=workn).values(
            'category__name', 'city',  'fullname', 'work_name', 'id')
        print(workt)
        print(workn)
        print(citty)
        print(names)
        
        return render(request, 'user_search_worker_table.html', {'names': names})
    else:
        return redirect('/')

def save_user_enquiry(request):
    if 'username2' in request.session:
        if request.session.has_key('username2'):
            username2 = request.session['username2']
        id = request.GET.get('tid')           
        v = enquiry()
        var=user_register.objects.get(id=username2)
        v.user_id_id= var.id
        v.worker_id_id=id
        v.enquiry=request.POST.get('enquiry1')
        v.status=0
        v.save()
        return redirect('user_search_worker')
    else:
        return redirect('/')
        

def user_worker_profile(request,id):
    if 'username2' in request.session:
        if request.session.has_key('username2'):
            username2 = request.session['username2']
        z = user_register.objects.filter(id=username2)
        mem= user_register.objects.get(id=id)
        return render(request,'user_worker_profile.html', {'z': z,'mem':mem})
    else:
        return redirect('/')

def user_worker_reports(request,id):
    if 'username2' in request.session:
        if request.session.has_key('username2'):
            username2 = request.session['username2']
        z = user_register.objects.filter(id=username2)
        mem= user_register.objects.get(id=id)
        mem1=feedback.objects.filter(worker_id=mem.id,replay_status=2)

        return render(request,'user_worker_reports.html', {'z': z,'mem1':mem1})
    else:
        return redirect('/')

def user_history_list(request):
    if 'username2' in request.session:
        if request.session.has_key('username2'):
            username2 = request.session['username2']
        if request.session.has_key('username'):
            username = request.session['username']
        z = user_register.objects.filter(id=username2)
        mem= feedback.objects.filter(user_id_id=username2,work_status='1').exclude(replay_status='0')
        return render(request,'user_history_list.html', {'z': z,'mem':mem})
    else:
        return redirect('/')

def user_post_feedback(request):
    if 'username2' in request.session:
        if request.session.has_key('username2'):
            username2 = request.session['username2']
        if request.session.has_key('username'):
            username = request.session['username']
        z = user_register.objects.filter(id=username2)
        mem= feedback.objects.filter(user_id_id=username2,work_status='1').exclude(replay_status='2')
        return render(request,'user_post_feedback.html', {'z': z,'mem':mem})
    else:
        return redirect('/')
def save_user_feedback(request):
    if 'username2' in request.session:
        if request.session.has_key('username2'):
            username2 = request.session['username2']
        tid = request.GET.get('tid')
        vars = feedback.objects.get(id=tid)
        print(vars.id)
        vars.replay_date=datetime.now()
        vars.feedback_replay = request.POST.get('feedback')
        vars.replay_status = 2
        print('hello')
        vars.save()
        return redirect('user_post_feedback')
    else:
        return redirect('/')
        
    ######################worker##########
    
def worker_dashboard(request):
    if 'usernamew2' in request.session:
        if request.session.has_key('usernamew2'):
            usernamew2 = request.session['usernamew2']
        z = user_register.objects.filter(id=usernamew2)
        return render(request,'worker_dashboard.html', {'z': z})
    else:
        return redirect('/')


def worker_view_edit_details(request):
    if 'usernamew2' in request.session:
        if request.session.has_key('usernamew2'):
            usernamew2 = request.session['usernamew2']
        z = user_register.objects.filter(id=usernamew2)
        return render(request,'worker_view_edit_details.html', {'z': z})
    else:
        return redirect('/')

def worker_edit_work_details(request):
    if 'usernamew2' in request.session:
        if request.session.has_key('usernamew2'):
            usernamew2 = request.session['usernamew2']
        z = user_register.objects.filter(id=usernamew2)
        mem= category.objects.filter().exclude(name='user')
        if request.method == 'POST':         
            v = user_register.objects.get(id=usernamew2)
            v.work_name=request.POST['workname']
            v.experience=request.POST['experience']
            v.city=request.POST['city']
            ut=user_register.objects.get(id=request.POST['category'])
            v.category_id= ut.id
            v.save()
            
        return render(request,'worker_edit_work_details.html', {'z': z,'mem':mem})
    else:
        return redirect('/')

def worker_user_enquiry_list(request):
    if 'usernamew2' in request.session:
        if request.session.has_key('usernamew2'):
            usernamew2 = request.session['usernamew2']
        z = user_register.objects.filter(id=usernamew2)
        mem = enquiry.objects.filter(worker_id_id=usernamew2,status=0)
        if request.method == 'POST':
            id = request.GET.get('tid')           
            v = enquiry.objects.get(id=id)
            v.enquiry_reply=request.POST['reply']
            v.status=1
            v.save()
        return render(request,'worker_user_enquiry_list.html', {'z': z,'mem':mem})
    else:
        return redirect('/')

def worker_history_list(request):
    if 'usernamew2' in request.session:
        if request.session.has_key('usernamew2'):
            usernamew2 = request.session['usernamew2']
        z = user_register.objects.filter(id=usernamew2)
        mem = feedback.objects.filter(worker_id=usernamew2,work_status=1).exclude(replay_status=0)
        return render(request,'worker_history_list.html', {'z': z,'mem':mem})
    else:
        return redirect('/')

def worker_post_feedback(request):
    if 'usernamew2' in request.session:
        if request.session.has_key('usernamew2'):
             usernamew2 = request.session['usernamew2']
        z = user_register.objects.filter(id=usernamew2)
        mem = feedback.objects.filter(worker_id_id=usernamew2,work_status=1).exclude(replay_status=0)
        if request.method == 'POST':
            id = request.GET.get('tid')           
            v = feedback.objects.get(id=id)
            v.feedback=request.POST['feedback']
            v.replay_status=1
            v.post_date=datetime.now()
            v.save()
            msg_success = " Feedback Posted successfully"
            return render(request, 'worker_post_feedback.html', {'z': z,'mem':mem,'msg_success': msg_success})
        return render(request,'worker_post_feedback.html', {'z': z,'mem':mem})
    else:
        return redirect('/')

def worker_work_status_cards(request):
    if 'usernamew2' in request.session:
        if request.session.has_key('usernamew2'):
            usernamew2 = request.session['usernamew2']
        z = user_register.objects.filter(id=usernamew2)
        return render(request,'worker_work_status_cards.html', {'z': z})
    else:
        return redirect('/')

def worker_curent_work(request):
    if 'usernamew2' in request.session:
        if request.session.has_key('usernamew2'):
            usernamew2 = request.session['usernamew2']
        z = user_register.objects.filter(id=usernamew2)
        return render(request,'worker_curent_work.html', {'z': z})
    else:
        return redirect('/')
    
def worker_completed_workes(request):
    if 'usernamew2' in request.session:
        if request.session.has_key('usernamew2'):
            usernamew2 = request.session['usernamew2']
        z = user_register.objects.filter(id=usernamew2)
        mem = feedback.objects.filter(worker_id_id=usernamew2,work_status=1)
        return render(request,'worker_completed_workes.html', {'z': z,'mem':mem})
    else:
        return redirect('/')

def worker_curent_ongoingworks(request):
    if 'usernamew2' in request.session:
        if request.session.has_key('usernamew2'):
            usernamew2 = request.session['usernamew2']
        z = user_register.objects.filter(id=usernamew2)
        mem = feedback.objects.filter(worker_id_id=usernamew2,work_status=0)
        if request.method == 'POST':
            id = request.GET.get('tid')
            
            v = feedback.objects.get(id=id)
            v.work_status=1
            v.to_date=datetime.now()
            v.save()
            msg_success = " Work Completed successfully"
            return render(request, 'worker_curent_ongoingworks.html', {'z': z,'mem':mem,'msg_success': msg_success})
        return render(request,'worker_curent_ongoingworks.html', {'z': z,'mem':mem})
    else:
        return redirect('/')

def worker_curent_addwork(request):
    if 'usernamew2' in request.session:
        if request.session.has_key('usernamew2'):
            usernamew2 = request.session['usernamew2']
        z = user_register.objects.filter(id=usernamew2)
        des= category.objects.get(name='user')
        mem= user_register.objects.filter(category_id=des.id) 
        pb=feedback()
        if request.method == 'POST':
            var=user_register.objects.get(id=usernamew2)         
            pb.worker_id_id = var.id
            pb.from_date=request.POST['fromdate']
            pb.work=request.POST['work']
            ut=user_register.objects.get(id=request.POST['user'])
            print(ut)
            pb.work_status=0
            pb.replay_status=0
            pb.user_id_id= ut.id
            pb.save()
            msg_success = "New Work Added successfully"
            return render(request, 'worker_curent_addwork.html', {'z': z,'mem':mem,'msg_success': msg_success})
        return render(request, 'worker_curent_addwork.html', {'z': z,'mem':mem})
    else:
        return redirect('/')
