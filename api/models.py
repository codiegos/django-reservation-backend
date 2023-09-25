from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

class Cabin(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(blank=True, max_length=200)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    cabin = models.ForeignKey(Cabin, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    tinaja = models.BooleanField(default=False)
    amount = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)
    message = models.CharField(blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cabin.name + ' - ' + self.customer.name

class Prepaid(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.name + ' - ' + str(self.amount)
    
class Setting(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.key + ': ' + self.value

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username