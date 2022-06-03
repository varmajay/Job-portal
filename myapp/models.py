from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
# from django.utils.translation import ugettext_lazy as _

# Create your models here.


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    GENDER = (
        (0,'Male'),
        (1,'Female'),
        )
 
    role = models.CharField(max_length=10 ,default='hr' )
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15,default=None,blank=True,null=True)
    gender = models.IntegerField(choices=GENDER,default=None,null=True,blank=True)
    address = models.TextField(default=None,blank=True,null=True)
    profile = models.FileField(upload_to='user',default='profile.png')
    
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return  self.name +" "+ self.email



class Jobs(models.Model):
    TYPE = (
        ('full-time', 'Full-Time'),
        ('part-time', 'Part-Time'),
        ('internship', 'Internship'),
    )
    CATEGORIES = (
        ('marketing','Marketing'),
        ('customer service','Customer Service'),
        ('human resource','Human Resource'),
        ('project management','Project Management'),
        ('business devlopment','Business Devlopment'),
        ('sales & communication','Seles & Communication'),
        ('teaching & education','Teaching & Education'),
        ('information technology','Information Technology'),
    )
    hr = models.ForeignKey(User,on_delete=models.CASCADE)
    categories = models.CharField(max_length=50,choices=CATEGORIES)
    type = models.CharField(max_length=30, choices=TYPE)
    position = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    job_description = models.TextField()
    experience = models.CharField(max_length=50)
    vacancy = models.IntegerField()
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.hr.name



class Application(models.Model):

    GENDER = (
        (0,'Male'),
        (1,'Female'),
        )

    job = models.ForeignKey(Jobs , on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.IntegerField(choices=GENDER)
    address = models.TextField()
    resume = models.FileField(upload_to='resume')


    def __str__(self):
        return self.name +'  '+ self.email







    
