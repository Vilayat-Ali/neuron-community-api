from django.db import models

class member(models.Model):
    
    image = models.CharField(max_length=100, default="https://bootdey.com/img/Content/avatar/avatar1.png")
    full_name = models.CharField(max_length=100, blank=False)
    role = models.CharField(max_length=100, blank=False)
    github = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.full_name