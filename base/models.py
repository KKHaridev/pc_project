from django.db import models
from django.db.models.fields import CharField
# Create your models here.
class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).upper()

class hospitals(models.Model):
    name = models.CharField(max_length=100)
    district = NameField(max_length=20)
    beds_available = models.IntegerField()
    def __str__(self):
        return self.name




