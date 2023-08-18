from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser
from .manager import CustomUserManger

class CustomUser(AbstractBaseUser,PermissionsMixin):
    USER_TYPE=(
        ('Patient','Patient'),
        ('Doctor','Doctor')
    )
    first_name=models.CharField(max_length=225,blank=True,null=True)
    last_name=models.CharField(max_length=225,blank=True,null=True)
    username=models.CharField(max_length=225,blank=True,null=True)
    address=models.CharField(max_length=225,blank=True,null=True)
    email=models.EmailField(unique=True)
    user_type1=models.CharField(max_length=25,default='',choices=USER_TYPE)
    image=models.ImageField(upload_to='profile_image',null=True,blank=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=CustomUserManger()

    class Meta:
        verbose_name = "All Users"
        verbose_name_plural = "All Users"

    def __str__(self):
        return f"{self.email}"
    
    