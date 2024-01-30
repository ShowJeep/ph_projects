from django.db import models
from category.models import Category
# Create your models here.
class Task(models.Model):
    Title= models.CharField(max_length= 50)
    Description= models.TextField(blank=True)
    is_completed= models.BooleanField(default= False)
    AssignDate= models.DateField(auto_now_add=True)
    category= models.ManyToManyField(Category)
    
    def __str__(self):
        return self.taskTitle