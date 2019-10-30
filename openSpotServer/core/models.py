from django.db import models


class Image(models.Model):
    objects = None
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
