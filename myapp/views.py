import random
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .forms import *
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required



# Create your views here.

# ------------------------------------Common Section -----------------------------------
def index(request):
    return render(request,'index.html')



@login_required(login_url='User_login')
def index_admin(request):
    return render(request,'superadmin/index.html')



def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        # print(form)
        if form.is_valid():
            user = authenticate(email = form.cleaned_data['email'],password = form.cleaned_data['password'])
            # print(user)
            if user is not None:
                if user.role == 'admin':
                    if user.is_active:
                        login(request, user)
                        return redirect('index_admin')
                else:
                    if user.is_active:
                        login(request, user)
                        return redirect('index')
            else:
                msg = "Enter correct username or password"
                return render(request,'login.html',{'form':form,'msg':msg})
        msg = "Enter correct username or password 2"
        return render(request,'login.html',{'form':form,'msg':msg})
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})


def user_logout(request):
    logout(request)
    return redirect('index') 





# ------------------------------------------Admin----------------------------------------------------

@login_required(login_url='/user_login/')
def admin_profile(request):
    return render(request,'superadmin/profile.html')

@login_required(login_url='/user_login/')
def view_hr(request):
    uid = User.objects.filter(role='hr')
    # print(uid)
    return render(request,'superadmin/view-hr.html',{'uid':uid})


@login_required(login_url='/user_login/')
def edit_hr(request,pk):
    hr = User.objects.get(id=pk)
    if request.method =="POST":
        form = Edit_hrForm(request.POST,instance=hr)
        if form.is_valid():
            form.save()
            messages.success(request,'HR profile update sucessfully ')
            return redirect('view_hr')
        else:
            messages.info(request,' Please Enter the valid data')
            return render(request,'admin/edit-hr.html',{'form':form})     
    else:
        form = Edit_hrForm(instance=hr)
    return render(request,'superadmin/edit_hr.html',{'form':form})
    


def delete_hr(request,pk):
    hr = User.objects.get(id=pk)
    hr.delete()
    messages.info(request,'Hr delete sucessfully')
    return redirect('view_hr')



@login_required(login_url='/user_login/')
def view_app(request):
    uid = Application.objects.all()
    return render(request,'superadmin/view-application.html',{'uid':uid})


# ------------------------------------------------HR----------------------------------------------------

def register(request):
    # print(form)
    if request.method == "POST":
        form= RegisterFrom(request.POST)
        # print(form)
        if form.is_valid():
            message = f"""Hello your username is {form.cleaned_data['email']},
            and Your password is {form.cleaned_data['password1']}"""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form.cleaned_data['email'],]
            send_mail( "your login details", message, email_from, recipient_list ) 
            form.save()
            messages.success(request,'your account created')
            return redirect('user_login')
        else:
            messages.error(request,form.errors)
            print(messages.error(request,form.errors))
            return render(request,'hr/register.html',{'form':form})
    else:
        form= RegisterFrom()
    return render(request,'hr/register.html',{'form':form})






@login_required(login_url='/user_login/')
def hr_profile(request):
    if request.method =="POST":
        form = HrprofileForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Update sucessfully')
            return redirect('hr_profile')
        else:
            messages.success(request,'Invalid Data')
            return render(request,'hr/hr_profile.html',{'form':form})
    else:
        form = HrprofileForm(instance=request.user)
    return render(request,'hr/hr_profile.html',{'form':form})




@login_required(login_url='/user_login/')
def job_post(request):
    if request.method =="POST":
        form = JobpostForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.hr = request.user
            temp.save()
            messages.success(request,'Job sucessfully Post')
            return redirect('job_post')
        else:
            messages.info(request,'Please Enter a Valid Data')
            return render(request,'hr/job-post.html',{'form':form})
    else:
        form = JobpostForm()
    return render(request,'hr/job-post.html',{'form':form})




@login_required(login_url='/user_login/')
def view_job_post(request):
    uid = Jobs.objects.filter(hr = request.user)
    return render(request,'hr/view-job-post.html',{'uid':uid})



def update_job_post(request,pk):
    job = Jobs.objects.get(id=pk)
    if request.method == "POST":
        form = UpdateJobForm(request.POST,instance=job)
        if form.is_valid():
            form.save()
            messages.success(request,'Job sucessfully Update')
            return redirect('view_job_post')
        else:
            messages.info(request,'Please Enter a Valid Data')
            return render(request,'hr/update_job_post.html',{'form':form})
    else:
        form = UpdateJobForm(instance=job)
    return render(request,'hr/update_job_post.html',{'form':form})


@login_required(login_url='/user_login/')
def delete_job_post(request,pk):
    post = Jobs.objects.get(id=pk)
    post.delete()
    messages.info(request,'Job Post deleted Sucessfullly ')
    return redirect('view_job_post')


@login_required(login_url='/user_login/')
def view_application(request):
    uid = Application.objects.filter(job__hr = request.user)
    return render(request,'hr/view-application-hr.html',{'uid':uid})



@login_required(login_url='/user_login/')
def forget_password(request):
    if request.method =="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            password = ''.join(random.choices('qwyertovghlk34579385',k=9))
            subject="Rest Password"
            message = f"""Hello {user.name},Your New password is "{password}" """
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'],]
            send_mail( subject, message, email_from, recipient_list )
            user.password = make_password(password)
            user.save()
            messages.success(request,'New password send in your email')
            return redirect('user_login')
        except:
            messages.info(request,'Enter the valid email addres')
            return render(request,'hr/forget-password.html')   
           
    return render(request,'hr/forget_password.html')   



@login_required(login_url='/user_login/')
def change_password(request):
    password=ChangePassword(user=request.user)
    if request.method == "POST":
        password1=ChangePassword(data=request.POST,user=request.user)
        if password1.is_valid():
            update_session_auth_hash(request,password1.user)
            password1.save()
            messages.success(request,'Your password has been change')
            return redirect('user_login')
        else:
            print(password1.errors)
            messages.info(request,'Enter the correct password') 
            return render(request,'hr/change-password.html',{'form':password})      
    return render(request,'hr/change-password.html',{'form':password})

# ------------------------------------------Job finder--------------------------------------

def job_filter(request,id):
    if id =='0':
        job=Jobs.objects.all()
        return render(request,'find_job.html',{'job':job}) 
    elif id =='1':
        job=Jobs.objects.filter(categories='marketing')
        return render(request,'find_job.html',{'job':job})
    
    elif id =='2':
       job=Jobs.objects.filter(categories='customer service')
       return render(request,'find_job.html',{'job':job})
   
    elif id =='3':
        job=Jobs.objects.filter(categories='human resource')
        return render(request,'find_job.html',{'job':job})
    elif id =='4':
        job=Jobs.objects.filter(categories='project management')
        return render(request,'find_job.html',{'job':job})

    elif id =='5':
        job=Jobs.objects.filter(categories='business devlopment')
        return render(request,'find_job.html',{'job':job})
    
    elif id =='6':
        job=Jobs.objects.filter(categories='sales & communication') 
        return render(request,'find_job.html',{'job':job})   
    
    elif id =='7':
        job=Jobs.objects.filter(categories='teaching & education')
        return render(request,'find_job.html',{'job':job})
    
    else: 
        job=Jobs.objects.filter(categories='information technology')
        return render(request,'find_job.html',{'job':job}) 





def find_job(request,pk):
    uid = Jobs.objects.get(id=pk)
    if request.method == "POST":
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            message = f"""Hello {form.cleaned_data['name']},
             Thank you for applying we will reach you soon...."""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form.cleaned_data['email'],]
            send_mail( "sucessfully Apply ", message, email_from, recipient_list )
            temp = form.save(commit=False)
            temp.job = uid
            temp.save()
            messages.success(request,'Sucessfully  Apply')
            return redirect('index')
        else:
            messages.info(request,'Invalid data')
            print(form)
            return render(request,'apply.html',{'form':form})
    else:
        form = ApplyForm()
    return render(request,'apply.html',{'form':form,'uid':uid})