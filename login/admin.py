# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import signup,Profile,Qualification,Teaching,Project,Publication,Experience

admin.site.register(signup)
admin.site.register(Profile)
admin.site.register(Qualification)
admin.site.register(Teaching)
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(Experience)