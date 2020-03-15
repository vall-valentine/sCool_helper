from django.apps import AppConfig
from django.db import models


# Create your models here.
class User(models.Model):
    id = models.IntegerField("id", primary_key=True)
    login = models.TextField("login", max_length="50")
    password = models.TextField("password", max_length="50")


class WeekDay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.IntegerField("id", primary_key=True)
    name = models.TextField("name", max_length="20")


class Lesson(models.Model):
    day = models.ForeignKey(WeekDay, on_delete=models.CASCADE)
    id = models.IntegerField("id", primary_key=True)
    name = models.TextField("name", max_length="50")


class HomeTask(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    id = models.IntegerField("id", primary_key=True)
    task = models.TextField("task", max_length="500")
    done = models.BooleanField("done")


class Note(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    id = models.IntegerField("id", primary_key=True)
    note = models.TextField("note", max_length="500")