from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from sqlalchemy import null
# Create your models here.


class Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="about")
    about = models.TextField()
   

    def __str__(self):
        return self.about
    