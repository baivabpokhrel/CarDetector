from django.db import models
from django.core.validators import int_list_validator


class Image(models.Model):
    objects = None
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255, blank=True)
    masked = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class Stats(models.Model):
    openSpotsList = models.CharField(validators=[int_list_validator], max_length=255)
    takenSpotsList = models.CharField(validators=[int_list_validator], max_length=255)
    openSpots = models.IntegerField()
    totalSpots = models.IntegerField()
    updatedAt = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, openSpots, totalSpots, openSpotsList, takenSpotsList):
        stats = cls(openSpots=openSpots, totalSpots=totalSpots, openSpotsList=openSpotsList, takenSpotsList=takenSpotsList)
        return stats
