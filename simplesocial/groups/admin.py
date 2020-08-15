from simplesocial.groups.models import GroupMemeber
from django.contrib import admin

# Register your models here.
from . import models

class GroupMemeberInLine(admin.TabularInline):
    model = models.GroupMemeber

admin.site.register(models.Group)