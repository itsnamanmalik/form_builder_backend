from django.contrib import admin
from form.models import Form, FormField, FormSubmission, SubmissionField


class FormFieldAdmin(admin.TabularInline):
    model = FormField

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    inlines = [FormFieldAdmin]
    list_display = ('name', 'description', 'created_by', 'created_at', 'updated_at', 'is_active')
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'created_by', 'created_at', 'updated_at',)
    

class SubmissionFieldAdmin(admin.TabularInline):
    model = SubmissionField    

@admin.register(FormSubmission)
class FormSubmissionAdmin(admin.ModelAdmin):
    inlines = [SubmissionFieldAdmin]
    list_display = ('form', 'submitted_by', 'created_at', 'updated_at')
    list_filter = ('form', 'created_at', 'updated_at',)
    
