from django.db import models

class applicant(models.Model):
    full_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)
    phone = models.CharField(max_length=15, blank=False, null=False) 
    description = models.TextField(max_length=400, blank=True, null=True)  

    def __str__(self):
        return self.full_name
