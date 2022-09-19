from pickle import TRUE
from tkinter import CASCADE
from django.db import models

# Create your models here.


class Tweet(models.Model):
    content = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)


class stadiumsModel(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    capacity = models.CharField(max_length=10)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class teamsModel(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    stadium = models.ForeignKey(stadiumsModel, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=15)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class playersModel(models.Model):
    name = models.CharField(max_length=30)
    team = models.ForeignKey(teamsModel, on_delete=models.CASCADE)
    age = models.CharField( max_length=3)
    position = models.CharField(max_length=20)
    number = models.CharField(max_length=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name