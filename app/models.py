from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='static/images', default='static/images/default.png')
    parish_name = models.CharField(max_length=255)
    parish_location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    

class AreaRecord(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    WEEK_CHOICES = (
        ('WEEK 1', 'WEEK 1'),
        ('WEEK 2', 'WEEK 2'),
        ('WEEK 3', 'WEEK 3'),
        ('WEEK 4', 'WEEK 4'),
        ('WEEK 5', 'WEEK 5'),
    )
    MONTH_CHOICES = (
        ('Jan', 'jan'),
        ('Feb', 'feb'),
        ('Mar', 'mar'),
        ('Apr', 'apr'),
        ('May', 'may'),
        ('Jun', 'jun'),
        ('Jul', 'jul'),
        ('Aug', 'aug'),
        ('Sep', 'sep'),
        ('Oct', 'oct'),
        ('Nov', 'nov'),
        ('Dec', 'dec'),
    )
    week = models.CharField(max_length=7, choices=WEEK_CHOICES) 
    month = models.CharField(max_length=4, choices=MONTH_CHOICES) 
    area_name = models.CharField(max_length=100)
    parish_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    area_coordinator = models.CharField(max_length=100)
    parish_number_with_report = models.PositiveIntegerField(default=0)
    parish_number_with_no_report = models.PositiveIntegerField(default=0)
    total_number_of_parish = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return f'{self.area_name} -[{self.area_coordinator}]'
    
    