#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from moevmCommon.models.userProfile import UserProfile

class AcademicDiscipline(models.Model):
  name = models.CharField(max_length=150)

  def __str__(self):
    return self.name


class AcademicDisciplineOfTeacher(models.Model):
  teacher = models.ForeignKey(UserProfile)
  disc = models.ForeignKey(AcademicDiscipline)
  #Вид занятия
  type = models.CharField(
    max_length=40,
  )
  characterUpdate = models.CharField(max_length=250)
  completeMark = models.BooleanField(default=False)