from django import views
from django.contrib import admin
from django.urls import path
from my_app import views
from django.conf import settings
from django.conf.urls.static import static, serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Login,name="Login"),
    path('Register/',views.Register,name="Register"),
    path('logout/', views.logout, name='logout'),

#######################admin##############################
    path('admin_dashboard/', views.admin_dashboard , name='admin_dashboard'),
    path('admin_new_worker_aprove/', views.admin_new_worker_aprove, name='admin_new_worker_aprove'),
    path('admin_worker_status_cards/', views.admin_worker_status_cards, name='admin_worker_status_cards'),
    path('admin_users_details/', views.admin_users_details, name='admin_users_details'),
    path('admin_user_profile_view/<int:id>/', views.admin_user_profile_view, name='admin_user_profile_view'),
    path('admin_worker_profile_view/<int:id>/', views.admin_worker_profile_view, name='admin_worker_profile_view'),
    path('admin_workers_details/', views.admin_workers_details, name='admin_workers_details'),
    path('admin_workers_register/', views.admin_workers_register, name='admin_workers_register'),
    path('admin_user_activity/', views.admin_user_activity, name='admin_user_activity'),
    path('admin_feedback_cards/', views.admin_feedback_cards, name='admin_feedback_cards'),
    path('admin_workers_feedbacks/', views.admin_workers_feedbacks, name='admin_workers_feedbacks'),
    path('admin_users_feedbacks/', views.admin_users_feedbacks, name='admin_users_feedbacks'),
    path('admin_all_workers/', views.admin_all_workers, name='admin_all_workers'),
    path('admin_all_contractors/', views.admin_all_contractors, name='admin_all_contractors'),
    path('admin_aproved_workers/', views.admin_aproved_workers, name='admin_aproved_workers'),
    path('admin_rejected_workers/', views.admin_rejected_workers, name='admin_rejected_workers'),
    path('reject_worker/', views.reject_worker, name='reject_worker'),



#############################user##########################
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('user_search_worker/', views.user_search_worker, name='user_search_worker'),
    path('user_search_worker_table/', views.user_search_worker_table, name='user_search_worker_table'),
    path('user_worker_profile/', views.user_worker_profile, name='user_worker_profile'),
    path('user_worker_reports/', views.user_worker_reports, name='user_worker_reports'),
    path('user_history_list/', views.user_history_list, name='user_history_list'),
    path('user_post_feedback/', views.user_post_feedback, name='user_post_feedback'),
    path('save_user_feedback/', views.save_user_feedback, name='save_user_feedback'),

############################worker########################
    path('worker_dashboard/', views.worker_dashboard, name='worker_dashboard'),
    path('worker_work_details_cards/', views.worker_work_details_cards, name='worker_work_details_cards'),
    path('worker_post_work_details/', views.worker_post_work_details, name='worker_post_work_details'),
    path('worker_view_edit_details/', views.worker_view_edit_details, name='worker_view_edit_details'),
    path('worker_edit_work_details/', views.worker_edit_work_details, name='worker_edit_work_details'),
    path('worker_user_enquiry_list/', views.worker_user_enquiry_list, name='worker_user_enquiry_list'),
    path('worker_history_list/', views.worker_history_list, name='worker_history_list'),
    path('worker_feedback_cards/', views.worker_feedback_cards, name='worker_feedback_cards'),
    path('worker_post_feedback/', views.worker_post_feedback, name='worker_post_feedback'),
    path('worker_view_feedback/', views.worker_view_feedback, name='worker_view_feedback'),
    path('worker_work_status_cards/', views.worker_work_status_cards, name='worker_work_status_cards'),
    path('worker_completed_workes/', views.worker_completed_workes, name='worker_completed_workes'),
    path('worker_curent_work/', views.worker_curent_work, name='worker_curent_work'),
    path('worker_curent_ongoingworks/', views.worker_curent_ongoingworks, name='worker_curent_ongoingworks'),
    path('worker_curent_addwork/', views.worker_curent_addwork, name='worker_curent_addwork'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)