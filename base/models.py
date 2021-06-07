from django.db import models
# Create your models here.
class hospitals(models.Model):
    name = models.CharField(max_length=100)
    district = models.CharField(max_length=20)
    beds = models.IntegerField()
    def __str__(self):
        return self.name