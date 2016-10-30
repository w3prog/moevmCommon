#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from moevmCommon.models.userProfile import UserProfile


class Publication(models.Model):
  name = models.CharField(max_length=250)
  user = models.ForeignKey(UserProfile)
  type = models.CharField(max_length=50)
  volume = models.IntegerField()
  publishingHouse = models.CharField(max_length=250)