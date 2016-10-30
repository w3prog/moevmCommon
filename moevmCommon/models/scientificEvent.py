#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from moevmCommon.models.userProfile import UserProfile

EVENT_TYPE_CHOISES = (
  ('k','Конкурс'),
  ('v','Выставка'),
  ('с','Конференция'),
  ('q','Семинар'),
)

reIter = (
        ('disposable', 'одноразовый'),
        ('repeating', 'повторяющийся')
)

class ScientificEvent(models.Model):
  eventName = models.CharField(max_length=255)
  level = models.CharField(max_length=20)
  date = models.DateField("Дата проведения")  # дата проведения
  place = models.CharField("Место проведения", max_length="100")  # дата проведения
  type = models.CharField(
    max_length=1,
    choices=EVENT_TYPE_CHOISES,
    default='c'
  )

  @staticmethod
  def create(name, user=None, **params):
    scientificEvent = ScientificEvent.objects.create(
      eventName=params.get('eventName'),
      level=params.get('level'),
      date=params.get('date'),
      place=params.get('place'),
      type=params.get('type'),
    )

    scientificEvent.save()

    return scientificEvent

  def __str__(self):
    # todo проверить корректность вывода
    return self.type + " " + self.level + " " + self.eventName


class Participation(models.Model):
  scientificEvent = models.ForeignKey(ScientificEvent)
  user = models.ForeignKey(UserProfile)
  title = models.CharField(max_length=250,null=True)

  @staticmethod
  def create(**params):
    participation = Participation.objects.create(
      scientificEvent=params.get('scientificEvent'),
      user=params.get('user'),
      title=params.get('title'),
    )

  def __str__(self):
    return self.user + " на " + self.scientificEvent.eventName