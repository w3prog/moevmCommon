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


class UserProfile(User):
    patronymic = models.CharField(max_length=30, null=True)
    birth_date = models.DateField(null=True)
    study_group = models.CharField(max_length=5, null=True)
    github_id = models.CharField(max_length=100, null=True)
    stepic_id = models.CharField(max_length=100, null=True)

    type = models.CharField(max_length=2, choices=PERSON_TYPE_CHOICES, default='s')

    # Дата текущего избрания или зачисления на преподавательскую должность
    election_date = models.DateField(null=True)

    # Должность
    position = models.CharField(max_length=40, null=True)

    # Срок окончания трудового договора
    contract_date = models.DateField(null=True)  # Возможн поменяю

    # Ученая степень
    academic_degree = models.CharField(max_length=1, choices=ACADEMIC_DEGREE_CHOICES, null=True)

    # Год присвоения ученой степени
    year_of_academic_degree = models.DateField(null=True)

    # Учебное звание
    academic_status = models.CharField(max_length=1, choices=ACADEMIC_STATUS_CHOICES, null=True)
    year_of_academic_status = models.DateField(null=True)

    @staticmethod
    def create(login, password, email, **params):
        user = UserProfile.objects.create_user(login, password, email)

        user.first_name = params.get('first_name')
        user.last_name = params.get('last_name')
        user.patronymic = params.get('patronymic')
        user.birth_date = params.get('birth_date')
        user.study_group = params.get('study_group')
        user.github_id = params.get('github_id')
        user.stepic_id = params.get('stepic_id')
        user.type = params.get('type', 's')
        user.election_date = params.get('election_date')
        user.position = params.get('position')
        user.contract_date = params.get('contract_date')
        user.academic_degree = params.get('academic_degree')
        user.year_of_academic_degree = params.get('year_of_academic_degree')
        user.academic_status = params.get('academic_status')
        user.year_of_academic_status = params.get('year_of_academic_status')

        user.save()

        return user

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.patronymic

    class Meta:
        db_table = 'userprofiles'


class AcademicDiscipline(models.Model):
  name = models.CharField(max_length=150)

  def __str__(self):
    return self.name


class AcademicDisciplineOfTeacher(models.Model):
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


class Publication(models.Model):
  name = models.CharField(max_length=250)
  user = models.ForeignKey(Person)
  type = models.CharField(max_length=50)
  volume = models.IntegerField()
  publishingHouse = models.CharField(max_length=250)
