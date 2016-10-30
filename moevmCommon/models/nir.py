#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from moevmCommon.models.userProfile import UserProfile

class NIR(models.Model):
  user = models.ForeignKey(UserProfile)
  workName = models.CharField(max_length=250)
  startDate = models.DateField()
  finishDate = models.DateField()
  role = models.CharField(max_length=100)
  organisation = models.CharField(max_length=250)