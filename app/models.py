from django.db import models

# Create your models here.
class Voter(models.Model):
    vname = models.CharField(max_length=50)
    vid = models.IntegerField(primary_key=True)
    vaddress = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.vname
