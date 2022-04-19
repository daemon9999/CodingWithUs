
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.


class Code(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="codes")
    title = models.CharField(max_length = 100)
    code = RichTextField()
    choices = [
        ("Java", "Java"),
        ("Python", "Python"),
        ("C#", "C#"),
        ("C++", "C++"),
        ("C", "C"),
        ("JavaScript", "JavaScript"),
        ("HtmlCss", "HtmlCss")
    ]
    code_language = models.CharField(max_length = 10, choices=choices)
    code_created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-code_created_date"]

class Comment(models.Model):
    code = models.ForeignKey(Code, on_delete = models.CASCADE, related_name="comments")
    comment_author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "comment")
    comment_content = models.TextField(null=True, blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["-comment_date"]
