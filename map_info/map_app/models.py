from django.db import models

class ParkInfo(models.Model):
    park_name = models.CharField(max_length=50, null=False, blank=False)
    playset_swing = models.CharField(max_length=10)
    playset_slide = models.CharField(max_length=10)
    playset_sandbox = models.CharField(max_length=10)
    vending_machine = models.CharField(max_length=10)
    water_services = models.CharField(max_length=10)
    bicycle_parking = models.CharField(max_length=10)
    parking = models.CharField(max_length=10)
    add_info = models.TextField()
    image = models.FileField(upload_to='picture/', null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=7)
    lng = models.DecimalField(max_digits=10, decimal_places=7)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.park_name
        



