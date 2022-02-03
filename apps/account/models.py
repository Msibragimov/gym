from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.

from apps.account.manager import UserManager


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(primary_key=True, max_length=15)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=True) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    bio = models.CharField(max_length=800)
    profile_photo = models.ImageField(upload_to='avatars/', null=True, default='avatar/ava.png')

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

