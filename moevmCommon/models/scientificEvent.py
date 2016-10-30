#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models

EVENT_TYPE_CHOISES = (
  ('k','Конкурс'),
  ('v','Выставка'),
  ('с','Конференция'),
)

class ScientificEvent(models.Model):
  eventName = models.CharField(max_length=255)
  level = models.CharField(max_length=20)
  title = models.CharField(
    max_length=250,
    null=True,
  )
  type = models.CharField(
    max_length=1,
    choices=EVENT_TYPE_CHOISES,
    default='c'
  )