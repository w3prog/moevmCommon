#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from moevmCommon.models.user_profile_manager import UserProfileManager

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
ACADEMIC_STATE_CHOICES  = (
  ('a','Аспирант'),
  ('d','Докторант'),
  ('s','Соискатель'),
  ('st','Стажер'),
)

class UserProfile(models.Model):
  user = models.OneToOneField(
    User,
    verbose_name="Ссылка на аккаунт для авторизации",
  )

  patronymic = models.CharField(
    max_length=30,
    null=True,
    verbose_name="Отчество",
  )
  birth_date = models.DateField(
    null=True,
    verbose_name="Дата рождения",
  )
  study_group = models.CharField(
    max_length=5,
    null=True,
    verbose_name="Учебная группа",
  )
  github_id = models.CharField(
    max_length=100,
    null=True,
    verbose_name="Профиль github",
  )
  stepic_id = models.CharField(
    max_length=100,
    null=True,
    verbose_name="Профиль stepic",
  )

  type = models.CharField(
    max_length=2,
    choices=PERSON_TYPE_CHOICES,
    default='s',
    verbose_name="Тип",
  )

  election_date = models.DateField(
    null=True,
    verbose_name="Дата текущего избрания или зачисления на преподавательскую должность",
  )

  position = models.CharField(
    max_length=40,
    null=True,
    verbose_name="Должность",
  )

  contract_date = models.DateField(
    null=True,
    verbose_name="Срок окончания трудового договора",
  )

  academic_degree = models.CharField(
    max_length=1,
    choices=ACADEMIC_DEGREE_CHOICES,
    null=True,
    verbose_name="Ученая степень",
  )

  year_of_academic_degree = models.DateField(
    null=True,
    verbose_name="Год присвоения ученой степени",
  )

  academic_status = models.CharField(
    max_length=1,
    choices=ACADEMIC_STATUS_CHOICES,
    null=True,
    verbose_name="Учебное звание",
  )

  year_of_academic_status = models.DateField(
    null=True,
    verbose_name="Год получения учебного звания",
  )

  academic_state = models.CharField(
    max_length=1,
    choices=ACADEMIC_STATE_CHOICES,
    null=True,
    verbose_name="Академическое положение",
  )

  profiles = UserProfileManager()
    
  @property
  def first_name(self):
    return self.user.first_name

  @property
  def last_name(self):
    return self.user.last_name

  @property
  def login(self):
    return self.user.username

  @property
  def password(self):
    return self.user.password

  @property
  def email(self):
    return self.user.email

  @property
  def FIO(self):
    first_name = last_name = patronymic= ""
    if not self.first_name == None : first_name = self.first_name
    if not self.last_name == None : last_name = self.last_name
    if not self.patronymic == None : patronymic = self.patronymic
    return first_name + ' ' + last_name + ' ' + patronymic

  def __str__(self):
    print self.type.__str__()
    if self.type.__str__() == 'a':
      return 'Администратор ' + self.FIO
    elif self.type.__str__() == 't':
      position = "Преподаватель"
      if not self.position == None: position = self.position
      return  position + " " + self.FIO
    elif self.type.__str__() == 'h':
      return "Староста группы " + self.study_group + " " + self.FIO
    elif self.type.__str__() == 's':
      group = ""
      if  not self.study_group == None:
        group = " группы " +self.study_group
      return "Студент" + group + " " + self.FIO
    else:
      return 'Неопознанный пользователь'

  def __unicode__(self):
    return unicode(self.user) or u''

  class Meta:
    db_table = 'userprofiles'
