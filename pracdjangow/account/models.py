from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self,email,username, sex,first_name, password=None):
        if not email:
            raise ValueError("user must have email")
        if not username:
            raise ValueError("user must have username")
        if not sex:
            raise ValueError("user must have sex")
        if not first_name:
            raise ValueError("user must have a firstname")

        user = self.model(
            email = self.normalize_email(email),
            username = self.username, 
            sex = self.sex,
            first_name = self.first_name
        )
        user.set_password(password)
        user.save(user = self._db)
        return user
        
    def create_superuser(self,email,username,first_name, sex, password):
        user = self.model(
            email = self.normalize_email(email),
            password = password,
            sex = sex,
            first_name = first_name
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email        = models.EmailField(verbose_name='email',max_length=60, unique=True)
    username     = models.CharField(max_length=30, unique=True)
    date_joined  = models.DateTimeField(verbose_name='date joined', auto_now=True)
    last_login   = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin     = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)
    is_staff     = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    sex          = models.CharField(max_length=6)
    first_name   = models.CharField(max_length=30)

    #login with email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','sex', 'first_name']

    object = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj =None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True
    