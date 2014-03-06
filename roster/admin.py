#!/usr/bin/env python

from django.contrib import admin
from roster.models import Student

class StudentAdmin(admin.ModelAdmin):
	search_fields = ('name',)
admin.site.register(Student, StudentAdmin)


