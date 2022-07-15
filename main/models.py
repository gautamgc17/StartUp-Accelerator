from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here

class Resources(models.Model):
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length=512)
    modules = models.IntegerField()
    link = models.URLField()

    class Meta:
        verbose_name_plural = "Resources"

    def __str__(self):
        return self.title

class StartUps(models.Model):
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length=512)
    link = models.URLField()

    class Meta:
        verbose_name_plural = "StartUps"

    def __str__(self):
        return self.title


class Schemes(models.Model):
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    scheme_name = models.CharField(max_length=255)
    organization = models.CharField(max_length = 100)
    description = models.CharField(max_length=1024)
    phone = models.CharField(max_length=12)
    mail = models.EmailField()
    link = models.URLField()

    class Meta:
        verbose_name_plural = "Schemes"

    def __str__(self):
        return self.organization

