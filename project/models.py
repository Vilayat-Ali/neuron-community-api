from django.db import models

class project(models.Model):
    title = models.CharField(max_length=150)
    image = models.CharField(max_length=200, default='https://picsum.photos/1000/1000')
    postedAt = models.DateField(auto_now_add=True)
    description = models.TextField()
    tags = models.JSONField(default=[{"tagName": "name of tag", "tagType": "tech, doc, web-app, package" }])

    def __str__(self):
        return self.title
