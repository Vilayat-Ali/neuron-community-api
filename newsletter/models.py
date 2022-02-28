from django.db import models
import uuid

class newsletter(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    email = models.EmailField(max_length=55)

    def __str__(self):
        return self.email

class important_problem(models.Model):
    full_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50, unique=True)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.email