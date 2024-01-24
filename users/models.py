from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The email field must be set")
        if not password:
            raise ValueError("Password must be provided")
        user = self.model(email=email, **extra_fields)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)



    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(email=email, password=password, **extra_fields)
    

def upload_to(instance, filename):
    return 'user/{filename}'.format(filename=filename)
    
# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # username = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to=upload_to,blank=True,null=True, default="avatar.svg")
    username = None

    USERNAME_FIELD = 'email'
    # USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
