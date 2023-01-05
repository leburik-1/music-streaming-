from django.db import models
from django.contrib.auth.models import AbstractUser
from utils import saveUserImage
from django.core.validators import FileExtensionValidator
from django.contrib.auth.base_user import BaseUserManager,AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self,username,email,age,password,**extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,age=age,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,age,password, **extra_fields):
        user = self.create_user(username,email,age,password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser,PermissionsMixin):
	email = models.EmailField(max_length = 254,unique=True)
	age = models.PositiveIntegerField()
	username = models.CharField(max_length=50, unique=True)
	date_joined = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	avatar = models.ImageField(upload_to=saveUserImage, validators=[FileExtensionValidator(allowed_extensions=["jpg","png","jpeg"])], null=True, blank=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['age','email']

	objects = UserManager()

	def __str__(self):
		return self.username
    
    

