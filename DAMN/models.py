from django.db import models


class Hospitals(models.Model):
    Name = models.CharField(max_length=200)

