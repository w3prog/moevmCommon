#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *


admin.site.register(Person)
admin.site.register(AcademicDiscipline)
admin.site.register(AcademicDisciplineOfTeacher)
admin.site.register(NIR)
admin.site.register(ScientificEvent)
admin.site.register(Publication)