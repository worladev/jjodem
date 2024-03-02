from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class CarType(models.Model):
    # image =
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        # return name
        pass


class Car(models.Model):
    # image =
    type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=200)
    number_of_doors = models.PositiveIntegerField()
    number_of_passengers = models.PositiveIntegerField()
    fuel = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    drive_type = models.CharField(max_length=50)

    def __str__(self):
        # return model_name
        pass
    # 1:28 on tutorial
