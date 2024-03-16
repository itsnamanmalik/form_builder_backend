from django.db import models
from common.models import BaseModel
from django.conf import settings
from django.contrib.postgres.fields import ArrayField


class Form(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class FormField(BaseModel):
    form = models.ForeignKey(to='form.Form', on_delete=models.CASCADE)
    field_type = models.ForeignKey(to='common.FieldType', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    placeholder = models.CharField(max_length=100, blank=True, null=True)
    help_text = models.TextField(blank=True, null=True)
    options = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    is_required = models.BooleanField(default=False)
    
    def __str__(self):
        return self.label
    

class FormSubmission(BaseModel):
    form = models.ForeignKey(to='form.Form', on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.form.name

class SubmissionField(BaseModel):
    form_submission = models.ForeignKey(to='form.FormSubmission', on_delete=models.CASCADE)
    form_field = models.ForeignKey(to='form.FormField', on_delete=models.CASCADE)
    value = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='form_submissions', blank=True, null=True)
    
    def __str__(self):
        return self.form_field.label