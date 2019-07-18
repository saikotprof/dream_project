from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    subject = models.CharField(max_length=500)
    content = models.TextField()
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:300]
