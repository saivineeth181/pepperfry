from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
# Customizing Django User Authentication

class UserManager(BaseUserManager):

    # creating user
    # this function will also called when we create super user

    def create_user(self, email,username, mobile_no, password=None):
        if not email:
            raise ValueError("email is required")
        if not mobile_no:
            raise ValueError("mobile number is required")
        if not username:
            raise ValueError("name is required")
        user = self.model(
            email=self.normalize_email(email[0]),
            username = username[0],
            mobile_no = int(mobile_no[0]),
        )
        user.set_password(password[0])
        user.save(using=self._db)
        return user

    #creating super user
    def create_superuser(self, email, username, mobile_no, password=None):

        if not email:
            raise ValueError("email is required")
        if not mobile_no:
            raise ValueError("mobile number is required")
        if not username:
            raise ValueError("name is required")
        user = self.model(
            email=self.normalize_email(email),
            username = username,
            mobile_no = int(mobile_no),
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):

    id = models.BigAutoField(primary_key=True)
    #users basic input
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    mobile_no = models.BigIntegerField()
    gender = models.CharField(max_length=10) 
    year = models.DateField(blank=True,null=True )
    about = models.TextField()
    profile_pic = models.ImageField()
    address = models.TextField()
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    #login and required field=
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile_no', 'username']
    objects = UserManager()

    # speical functions
    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
        
    class Meta:
        db_table = "UserDetail"
