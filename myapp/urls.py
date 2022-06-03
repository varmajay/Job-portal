from django.urls import path
from .import views

urlpatterns = [

    path('',views.index,name='index'),
    path('index_admin/',views.index_admin,name='index_admin'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),

    # ---------------------------Admin-----------------------------
    path('admin_profile/',views.admin_profile,name='admin_profile'),
    path('view_hr/',views.view_hr,name='view_hr'),
    path('edit_hr/<int:pk>',views.edit_hr,name='edit_hr'),
    path('delete_hr/<int:pk>',views.delete_hr,name='delete_hr'),
    path('view_app/',views.view_app,name='view_app'),


    # --------------------------hr-----------------------------------------
    path('register/',views.register,name='register'),
    path('hr_profile/',views.hr_profile,name='hr_profile'),
    path('view_application/',views.view_application,name='view_application'),
    path('job_post/',views.job_post,name='job_post'),
    path('view_job_post/',views.view_job_post,name='view_job_post'),
    path('update_job_post/<int:pk>',views.update_job_post,name='update_job_post'),
    path('delete_job_post/<int:pk>',views.delete_job_post,name='delete_job_post'),
    path('forget_password',views.forget_password,name='forget_password'),
    path('change_password',views.change_password,name='change_password'),

    # ---------------------------Job finder  -------------------------
    path('find_job/<int:pk>',views.find_job,name='find_job'),
    path('job_filter/<str:id>',views.job_filter,name='job_filter'),
    

]