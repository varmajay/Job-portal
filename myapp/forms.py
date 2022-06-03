from django import forms
from .models import*
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.forms import ModelForm

class LoginForm(forms.Form):
    email =forms.CharField()
    password= forms.CharField(
        widget=forms.PasswordInput(),
    )
    


        
# class Login(AuthenticationForm):
#     email=forms.CharField()
#     password=forms.CharField(label='Password',widget=forms.PasswordInput()) 
    

class RegisterFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','email','phone']


class Edit_hrForm(ModelForm):
    class Meta:
        model = User
        fields = ['name','email','phone','gender','address']



class HrprofileForm(ModelForm):
    class Meta:
        model = User
        fields = ['name','email','phone','gender','address','profile']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
                
        }



class JobpostForm(ModelForm):
    class Meta:
        model = Jobs
        fields =['categories','type','position','salary','job_description','experience','vacancy']
        widgets = {
            'categories': forms.Select(attrs={'class':'form-control'}),
            'type': forms.Select(attrs={'class':'form-control'}),
            'position': forms.TextInput(attrs={'class':'form-control'}),
            'salary': forms.TextInput(attrs={'class':'form-control'}),
            'job_description': forms.TextInput(attrs={'class':'form-control'}),
            'experience': forms.TextInput(attrs={'class':'form-control'}),
            'vacancy': forms.NumberInput(attrs={'class':'form-control'}),
                
        }


class UpdateJobForm(ModelForm):
    class Meta:
        model = Jobs
        fields =['categories','type','position','salary','job_description','experience','vacancy']
        widgets = {
            'categories': forms.Select(attrs={'class':'form-control'}),
            'type': forms.Select(attrs={'class':'form-control'}),
            'position': forms.TextInput(attrs={'class':'form-control'}),
            'salary': forms.TextInput(attrs={'class':'form-control'}),
            'job_description': forms.TextInput(attrs={'class':'form-control'}),
            'experience': forms.TextInput(attrs={'class':'form-control'}),
            'vacancy': forms.NumberInput(attrs={'class':'form-control'}),
                
        }


class ApplyForm(ModelForm):
    class Meta:
        model = Application
        fields =['name','email','phone','dob','gender','address','resume']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control','type': 'date'}),
            'gender': forms.Select(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'resume': forms.FileInput(attrs={'class':'form-control'}),
                
        }


class ChangePassword(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center'}),
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center'}),    
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center'}),    
    )