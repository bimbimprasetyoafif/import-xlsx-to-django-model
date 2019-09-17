from django.db import models

# Create your models here.
class CuriculumVitae(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=10)

    def __str__ (self):
        return self.name