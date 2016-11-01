#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
from moevmCommon.models.userProfile import *
from moevmCommon.models.academicDiscipline import *
from moevmCommon.models.nir import *
from moevmCommon.models.publication import *
from moevmCommon.models.scientificEvent import *
from django.contrib.auth.models import User
from faker import Faker


class Command(BaseCommand):
  """
  Данная команда необходима чтобы наполнить базу новыми данными.
  """

  def handle(self, *args, **options):
    """
    Данная процедура создает новые данные в базу
    :param args:
    :param options:
    :return:
    """
    faker = Faker()
    #todo реализовать процедуру.
    print faker.name()
    print("Случайные данные добавлены в базу данных")