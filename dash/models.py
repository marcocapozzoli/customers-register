from django.db import models
from datetime import datetime, timezone

class Person(models.Model):
    
    LABEL = (
        ('Frio','Frio'),
        ('Morno','Morno'),
        ('Quente','Quente'),
    )
    
    first_name = models.CharField(max_length=15, blank=False, null=False)
    last_name = models.CharField(max_length=15, blank=True, null=True, default='')
    birthday = models.DateField(null=True)
    email = models.EmailField()
    phone = models.IntegerField(blank=False, null=False)
    company_id = models.CharField(max_length=15, blank=False, null=False)
    label = models.CharField(max_length=6, choices=LABEL, blank=False, null=False, default='Frio')
    note = models.TextField(default='')
    photo = models.FileField(null=True)
    social_media = models.URLField(null=True)
    
    update_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name
