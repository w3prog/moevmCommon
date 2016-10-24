#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

PERSON_TYPE_CHOICES = (
    ('s', 'Студент'),
    ('h', 'Староста'),
    ('t', 'Преподаватель'),
    ('a', 'Администратор'),
)
ACADEMIC_STATUS_CHOICES  = (
  ('a','Ассистент'),
  ('s','Старший преподаватель'),
  ('d','Доцент'),
  ('p','Профессор'),
)

ACADEMIC_DEGREE_CHOICES = (
  ('n','Без степени'),
  ('t','Кандидат наук'),
  ('d','Доктор наук'),
)

EVENT_TYPE_CHOISES = (
  ('k','Конкурс'),
  ('v','Выставка'),
  ('с','Конференция'),
)


class Person(models.Model):
  firstName = models.CharField(max_length=20)
  lastName = models.CharField(max_length=20)
  user = models.ForeignKey(
    User,
    null=True
  )
  type = models.CharField(
    max_length=2,
    choices=PERSON_TYPE_CHOICES,
    default='s'
  )
  studyGroup = models.CharField(
    max_length=5,
    null=True
  )
  birstDate = models.DateField(null=True)
  #Дата текущего избрания или зачисления на преподавательскую должность
  electionDate = models.DateField(null=True)
  #Должность
  position = models.CharField(max_length=40,null=True)
  #Срок окончания трудового договора
  contractDate = models.DateField(null=True) # Возможн поменяю
  #Ученая степень
  academicDegree = models.CharField(
    max_length=1,
    choices=ACADEMIC_DEGREE_CHOICES,
    null=True
  )
  #Год присвоения ученой степени
  yearOfAcademicDegree = models.DateField(null=True)
  #Учебное звание
  academicStatus = models.CharField(
    max_length=1,
    choices=ACADEMIC_STATUS_CHOICES,
    null=True,
  )
  yearOfAcademicStatus = models.DateField(null=True)


  def __str__(self):
    return self.firstName + " " + self.lastName


class AcademicDiscipline(models.Model):
  name = models.CharField(max_length=150)

  def __str__(self):
    return self.name


class AcademicDisciplineOfTeachers(models.Model):
  teacher = models.ForeignKey(Person)
  disc = models.ForeignKey(AcademicDiscipline)
  #Вид занятия
  type = models.CharField(
    max_length=40,
  )
  characterUpdate = models.CharField(max_length=250)
  completeMark = models.BooleanField(default=False)


class NIR(models.Model):
  user = models.ForeignKey(Person)
  workName = models.CharField(max_length=250)
  startDate = models.DateField()
  finishDate = models.DateField()
  role = models.CharField(max_length=100)
  organisation = models.CharField(max_length=250)


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


class Publications(models.Model):
  name = models.CharField(max_length=250)
  user = models.ForeignKey(Person)
  type = models.CharField(max_length=50)
  volume = models.IntegerField()
  publishingHouse = models.CharField(max_length=250)