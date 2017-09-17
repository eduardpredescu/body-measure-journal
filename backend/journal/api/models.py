from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        # Ensure that an email address is set
        if not email:
            raise ValueError('Users must have a valid e-mail address')

        # Ensure that a username is set
        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username')

        account = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username'),
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password=None, **kwargs):
        account = self.create_user(email, password, kwargs)

        account.is_admin = True
        account.save()

        return account


class Account(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True)

    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Measurement(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    weight = models.IntegerField()
    height = models.IntegerField()
    waist_m = models.IntegerField()
    hip_m = models.IntegerField()
    bust_m = models.IntegerField()
    owner = models.ForeignKey('Account',on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.date)
