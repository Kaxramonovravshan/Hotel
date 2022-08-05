from pickle import TRUE
from django.utils import timezone
from django.db import models

class Feedback(models.Model):
    name = models.CharField('User name', max_length=256)
    number = models.IntegerField('Phone number', default=0, blank=True)
    number_person = models.IntegerField('Number person', default=0, blank=True)
    number_children = models.IntegerField('Number children', default=0, blank=True)
    select = models.CharField('Room', max_length=256, null=True)


    class Meta:
        verbose_name = 'Name'
        verbose_name_plural = 'Name'

    def __str__(self):
        return self.name
