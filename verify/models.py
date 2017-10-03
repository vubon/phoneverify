# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import signals
from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


def create_msg(sender, created, instance,**kwargs):
    print('Your Post has been created ')


def delete_msg(sender, instance, **kwargs):
    print('Your post has been deleted')


class Test_person(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

# Todo: Need to test  @receiver([post_save, post_delete], sender=User)
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)


signals.post_save.connect(create_msg, sender=Test_person)
signals.post_save.connect(create_msg, sender=Person)
signals.post_delete.connect(delete_msg, sender=Test_person)
signals.post_delete.connect(delete_msg, sender=Person)

