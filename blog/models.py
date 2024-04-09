from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Model class for blog post
    """
    title = models.CharField(max_length=100, unique=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
        sorted created date by latest
        """
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + ' | ' + str(self.created_on)