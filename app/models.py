from django.db import models
import re

from django.db.models.deletion import CASCADE
# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors={}
        if len(postData['first_name']) < 2:
            errors['first_name']='First name must be at least 2 characters'
        if len(postData['last_name']) < 2:
            errors['last_name']='Last name must be at least 2 characters'
        if not EMAIL_REGEX.match(postData['email']):        
            errors['email'] = ("Invalid email address!")
        elif User.objects.filter(email=postData['email']):
            errors['email'] = 'Email already exists'
        if len(postData['password'])< 8:
            errors['password']= 'Password must be at least 8 characters'
        elif postData['password'] != postData['confirmPW']:
            errors['password'] = 'Password and confirm password must match'
        return errors

    def account_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 1:
            errors["first_name"] = "First name cannot be blank"
        if len(postData['last_name']) < 1:
            errors["first_name"] = "Last name cannot be blank"
        if not EMAIL_REGEX.match(postData['email']):        
            errors['email'] = ("Invalid email address!")
        return errors
class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    #quotes = quotes associated to a user
    objects=UserManager()
    def __str__(self):
        return self.last_name, self.first_name

class Beer(models.Model):
    name=models.CharField(max_length=255)
    style=models.CharField(max_length=255)
    ABV=models.DecimalField(max_digits=3, decimal_places=1)
    description=models.TextField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    user=models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    beer=models.ForeignKey(Beer, related_name='orders', on_delete=CASCADE)
    table=models.IntegerField(default=None)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Order #{self.id} by {self.user.first_name} for Table #{self.table}'

