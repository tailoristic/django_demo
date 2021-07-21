from django.db import models

# Create your models here.
# Model class is a class which represents a database table.
# Each model is a python class that subclasses django.db.models.Model.
# Each attribute of the model represents a database field.
# With all the attributes of the model, we can create a database table.
# python manage.py makemigrations > will generate sql statemeents 
# python manage.py migrate > will migrate our changes to database (REGISTER WITH ADMIN URL)
# python manage.py createsuperuser > to create super user credentials for our admin panel


class Student(models.Model):
    studid = models.IntegerField()
    stuname = models.CharField(max_length=70)
    stuemail = models.EmailField(max_length=70)
    stupass = models.CharField(max_length=70)
    comment = models.CharField(max_length=40, default='not available')
    