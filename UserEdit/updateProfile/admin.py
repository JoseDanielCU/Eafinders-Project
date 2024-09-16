from django.contrib import admin
from .models import *


class Users(admin.ModelAdmin):
    pass


admin.site.register(UserRecords, Users)


# Register your models here.
