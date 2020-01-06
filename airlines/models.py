from django.db import models

# Create your models here.
class Airlines(models.Model):
    airways_name = models.CharField(max_length=200)
    airways_flight_code = models.CharField(max_length=200)
    airways_logo = models.ImageField(upload_to='photos/%airways/')
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return self.airways_name