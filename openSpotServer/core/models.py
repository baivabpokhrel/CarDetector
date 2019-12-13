from django.db import models


class Image(models.Model):
    objects = None
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255, blank=True)
    masked = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class Stats(models.Model):
    openSpots = models.IntegerField()
    totalSpots = models.IntegerField()
    updatedAt = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, openSpots, totalSpots):
        stats = cls(openSpots=openSpots, totalSpots=totalSpots)
        return stats
