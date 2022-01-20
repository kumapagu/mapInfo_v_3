from django.db import models

class Positions(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=7)
    lng = models.DecimalField(max_digits=10, decimal_places=7)

class ParkInfo(models.Model):
    park_name = models.CharField(max_length=50, default='公園')
    playset_swing = models.CharField(max_length=10)
    playset_slide = models.CharField(max_length=10)
    playset_sandbox = models.CharField(max_length=10)
    vending_machine = models.CharField(max_length=10)
    water_services = models.CharField(max_length=10)
    bicycle_parking = models.CharField(max_length=10)
    parking = models.CharField(max_length=10)
    add_info = models.TextField()
    image = models.FileField(null=True, upload_to='picture/')
    position = models.OneToOneField(Positions, on_delete=models.CASCADE)

    def __str__(self):
        return self.park_name
        



