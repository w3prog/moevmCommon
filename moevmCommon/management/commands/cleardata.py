#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
from moevmCommon.models.userProfile import *
from moevmCommon.models.academicDiscipline import *
from moevmCommon.models.nir import *
from moevmCommon.models.publication import *
from moevmCommon.models.scientificEvent import *
from django.contrib.auth.models import User

class Command(BaseCommand):
  """
  Данная команда необходима чтобы очистить базу данных
  """

  def handle(self, *args, **options):
    """
    Данная процедура создана чтобы очистить таблицы базы данных.
    :param args:
    :param options:
    :return:
    """
    User.objects.filter(is_superuser=False).delete()

    print("Данные успешно удалены")