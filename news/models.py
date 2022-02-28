from django.db import models

class community_new(models.Model):

    message = models.TextField(max_length=400)
    issuer = models.CharField(max_length=150)
    links = models.JSONField(default=[{"link": "link goes here", "message": "link message"}])
    date = models.DateField(auto_now_add=True)

    def __str__ (self):
        return self.message
