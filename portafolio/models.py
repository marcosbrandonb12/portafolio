from django.db import models

from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/images")
    url = URLField(blank=True)


class Portfolio(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    career = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)