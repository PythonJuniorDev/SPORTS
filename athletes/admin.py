from django.contrib import admin
from .models import Athlete, Instructor, Personal_access_code

admin.site.register(Athlete)
admin.site.register(Instructor)
admin.site.register(Personal_access_code)

