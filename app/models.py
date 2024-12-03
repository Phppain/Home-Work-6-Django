from django.db import models

class Parent(models.Model):
    class WhichParent(models.TextChoices):
        DAD = 'DD', 'Отец'
        MOM = 'MM', 'Мать'
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    parent = models.CharField(max_length=6, choices=WhichParent)
    phone_number = models.IntegerField()


class Child(models.Model):
    class Gender(models.TextChoices):
        MALE = 'ML', 'Мужской'
        FEMALE = 'FML', 'Женский'
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=7, choices=Gender)
