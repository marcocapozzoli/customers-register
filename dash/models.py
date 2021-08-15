from django.db import models
from datetime import datetime

class Person(models.Model):
    
    LABEL = (
        ('Frio','Frio'),
        ('Morno','Morno'),
        ('Quente','Quente'),
    )
    
    first_name = models.CharField(max_length=15, blank=False, null=False)
    last_name = models.CharField(max_length=15, blank=True, null=True)
    birthday = models.DateField(default=datetime.now)
    email = models.EmailField()
    phone = models.CharField(max_length=25, blank=False, null=False)
    company_id = models.CharField(max_length=15, blank=False, null=False)
    label = models.CharField(max_length=6, choices=LABEL, blank=False, null=False, default='Frio')
    update_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name
