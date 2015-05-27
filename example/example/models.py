# -*- coding: utf-8 -*-
from django.db import models


class Automobile(models.Model):
    car_bodies = (
        ('M', u'минивэн'),
        ('O', u'внедорожник'),
        ('U', u'универсал'),
        ('S', u'седан'),
        ('H', u'хэтчбэк')
    )
    gearbox_types = (
        ('M', u'механическая'),
        ('A', u'автоматическая')
    )
    manufacturer = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    car_body = models.CharField(max_length=1, choices=car_bodies)
    color = models.CharField(max_length=30)
    gearbox_type = models.CharField(max_length=1, choices=gearbox_types)
    amount = models.IntegerField()
    register_date = models.DateField(auto_now_add=True)
    engine_power = models.IntegerField()
    year = models.IntegerField()
    photo = models.ImageField(blank=True)


class Client(models.Model):
    genders = (
        ('M', u'мужской'),
        ('F', u'женской')
    )
    surname = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    gender = models.CharField(max_length=1, choices=genders)
    t_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    passport = models.CharField(max_length=10)
    inn = models.CharField(max_length=12)


class Contract(models.Model):
    status_types = (
        (True, u'оплачено'),
        (False, u'не оплачено')
    )
    amount = models.IntegerField()
    status = models.BooleanField(default=False, choices=status_types)
    description = models.TextField(max_length=30)
    auto_id = models.ForeignKey(Automobile)
    client_id = models.ForeignKey(Client)




