from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.account.manager import UserManager
# Create your models here.


class Account(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=15)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=True) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    bio = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to='images/', null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_perms(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

   