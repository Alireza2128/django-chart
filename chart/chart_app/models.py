from django.db import models

# Create your models here.
class country(models.Model):
    name = models.CharField(max_length=200 , verbose_name="country name " , unique=True)
    value = models.PositiveIntegerField(verbose_name="value of country ")

    def __str__(self):
        return self.name