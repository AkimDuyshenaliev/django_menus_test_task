from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.name


class Folder(models.Model):
    name = models.CharField(max_length=45)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name