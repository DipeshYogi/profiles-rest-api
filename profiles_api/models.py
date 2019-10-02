from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """manager for user profiles"""
    def create_user(self,email, name, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError("Users must have email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name = name)

        user.setpassword(password)
        user.save(using=self_db)

        return user

    def create_superuser(self,email,name,password):
        user =self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=244)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name"""
        return self.name

    def __str__(self):
        """return string representation of user"""
        return self.email
