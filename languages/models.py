from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Language(models.Model):
    language = models.CharField(max_length=40)
    language_detail = RichTextField(blank=True, null=True)
    language_fields = models.TextField(blank=True, null= True)
    

    def get_list(self):
        return self.language_fields.split(", ")

    def __str__(self):
        return self.language