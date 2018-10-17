from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Chart(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    type_chart = models.ForeignKey('TypeChart', on_delete=True)
    x_axis = models.CharField(max_length=50)
    y_axis = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TypeChart(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
