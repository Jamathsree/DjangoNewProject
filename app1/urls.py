from . import views
from django.urls import path

urlpatterns=[
    path('login_view',views.login_view,name='login_view'),
    path('logout_view',views.logout_view, name='logout_view'),
    ##############################ADMIN DASHBOARD########################
    path('',views.Home, name='Home'),
    path('admin_home',views.admin_home, name='admin_home'),
    path('add_services', views.add_services, name='add_services'),
    path('service_view',views.service_view,name="service_view"),
    path('service_delete/<int:id>/',views.service_delete,name='service_delete'),
    path('worker_register',views.worker_register,name='worker_register'),
    path('Worker_view',views.Worker_view,name='Worker_view'),
    path('Worker_edit_views/<int:id>/',views.Worker_edit_views,name='Worker_edit_views'),
    path('Worker_delete_views/<int:id>/', views.Worker_delete_views, name='Worker_delete_views'),
    path('Customer_view', views.Customer_view, name='Customer_view'),
    path('Customer_edit_views/<int:id>/', views.Customer_edit_views, name='Customer_edit_views'),
    path('Customer_delete_views/<int:id>/', views.Customer_delete_views, name='Customer_delete_views'),
    path('reply_complaint/<int:id>/', views.reply_complaint, name='reply_complaint'),
    path('View_reply', views.View_reply, name='View_reply'),

    ##############################ADMIN DASHBOARDS ENDS##########################

    path('Customer_register', views.Customer_register, name='Customer_register'),
    path('Customer_schedule_view', views.Customer_schedule_view, name='Customer_schedule_view'),
    # path('Customer_booking', views.Customer_booking, name='Customer_booking'),
    path('Schedule_add',views.Schedule_add,name='Schedule_add'),
    path('Worker_schedule_view',views.Worker_schedule_view,name='Worker_schedule_view'),
    path('Worker_schedule_edit/<int:id>/', views.Worker_schedule_edit, name='Worker_schedule_edit'),
    path('Worker_schedule_delete/<int:id>/', views.Worker_schedule_delete, name='Worker_schedule_delete'),
    path('view_appointment_worker', views.view_appointment_worker, name='view_appointment_worker'),
    path('accept/<int:id>/', views.accept, name='accept'),
    path('reject/<int:id>/', views.reject, name='reject'),


    path('Customer_home',views.Customer_home,name='Customer_home'),
    path('Customer_profile', views.Customer_profile, name='Customer_profile'),
    #####################################################Worker Dashboard######################################
    path('Worker_home',views.Worker_home,name='Worker_home'),
    path('Profile', views.Profile, name='Profile'),
    path('take_appointment/<int:id>/', views.take_appointment, name='take_appointment'),
    path('view_appointment_user', views.view_appointment_user, name='view_appointment_user'),
    path('Complaints', views.Complaints, name='Complaints'),
    path('View_complaint', views.View_complaint, name='View_complaint'),
]