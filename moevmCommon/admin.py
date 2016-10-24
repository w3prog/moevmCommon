#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from django.contrib import admin
from .models import *


admin.site.register(Person)
admin.site.register(AcademicDiscipline)
admin.site.register(AcademicDisciplineOfTeachers)
admin.site.register(NIR)
admin.site.register(ScientificEvent)
admin.site.register(Publications)