from django.contrib import admin
from common.models import FieldType


@admin.register(FieldType)
class FieldTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active')
    search_fields = ('name', 'description')
    list_filter = ('is_active',)