from core.models import ModelA, ModelB

from django.contrib import admin

from django.db import models

from typing import Type


def getFields(c: Type[models.Model]): 
    return [field.name for field in c._meta.get_fields() 
            if isinstance(field, models.Field) 
            and not isinstance(field, models.ManyToManyField)]


# @admin.register(ModelA)
class WheelAdmin(admin.ModelAdmin):
    list_display = getFields(ModelA)  # type: ignore
    list_filter = getFields(ModelA)  # type: ignore


# @admin.register(ModelB)
class StockAdmin(admin.ModelAdmin):
    list_display = getFields(ModelB)  # type: ignore
    list_filter = getFields(ModelB)  # type: ignore


