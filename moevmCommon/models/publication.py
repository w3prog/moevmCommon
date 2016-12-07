#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from moevmCommon.models.userProfile import UserProfile


TYPE_PUBLICATION_CHOICES = (
  ('guidelines', 'Методическое указание'),
  ('book', 'Книга'),
  ('journal', 'Статья в журнале'),
  ('compilation', 'Конспект лекции/сборник докладов'),
  ('collection ', 'Сборник трудов')
)

reIter = (
  ('disposable', 'одноразовый'),
  ('repeating', 'повторяющийся')
)


class Publication(models.Model):

  name = models.CharField(
    max_length=250,
    verbose_name="Название",
  )

  user = models.ForeignKey(
    UserProfile,
    null=True,
    verbose_name="Ссылка на автора",
  )

  # объем
  volume = models.IntegerField(
    "Объем",
    null=True,
    verbose_name = "Объем",

  )

  # название издательства
  publishingHouseName = models.CharField(
    "Название издательства",
    max_length="100",
    null=True,
    verbose_name="Название издательства",
  )

  publicationType = models.CharField(
    "Тип публикации",
    max_length="20",
    choices=TYPE_PUBLICATION_CHOICES,
    default="book",
    verbose_name="Тип публикации",
  )

  # вид повторения сборника
  reiteration = models.CharField(
    "Вид повторения сборника",
    choices=reIter,
    max_length="10",
    default="disposable",
    verbose_name = "Вид повторения сборника",
    )

  # номер издания
  number = models.IntegerField(
    "Номер издания",
    null=True,
    verbose_name = "Номер издания",
  )

  # место издания
  place = models.CharField(
    "Место издания",
    max_length="100",
    null=True,
    verbose_name="Место издания",
  )

  # дата издания
  date = models.DateField(
    "Дата издания",
    null=True,
    verbose_name="Дата издания",
  )

  # единицы объема
  unitVolume = models.CharField(
    "Единицы объёма",
    max_length="100",
    verbose_name="Единицы объёма",

  )
  # тираж
  edition = models.IntegerField(
    "Тираж",
    null=True,
    verbose_name="Тираж",
  )

  # вид методического издания / книги
  type = models.CharField(
    "Вид",
    max_length="100",
    # todo проверить как работает этот код
    help_text="Поле заполняется, если тип вашей публикации" " \"Книга\" или \"Методическое указание\"",
    null=True,
    verbose_name="Вид",
  )

  # ISBN
  isbn = models.CharField(
    "ISBN",
    max_length="100",
    # todo проверить как работает этот код
    help_text="Поле заполняется, если тип вашей публикации" "\"Книга\" или \"Методическое указание\"",
    null=True,
    verbose_name="ISBN",
  )

  # редактор сборника
  editor = models.CharField(
    "Редактор сборника",
    max_length="100",
    null=True,
    verbose_name="Редактор сборника",
  )

  @staticmethod
  def create(**params):
    publication = Publication.objects.create(
      name=params.get('name'),
      user=params.get('user'),
      volume=params.get('volume'),
      publishingHouseName=params.get('publishingHouseName'),
      publicationType=params.get('publicationType'),
      reiteration=params.get('reiteration'),
      number=params.get('number'),
      place=params.get('place'),
      date=params.get('date'),
      unitVolume=params.get('unitVolume'),
      edition=params.get('edition'),
      type=params.get('type'),
      isbn=params.get('isbn'),
      editor=params.get('editor'),
    )

    publication.save()

    return publication

  def __str__(self):
    return self.publicationType + ' ' + self.name + ' ' + self.isbn