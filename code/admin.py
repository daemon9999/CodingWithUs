from django.contrib import admin
from .models import Code, Comment
# Register your models here.

@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    class Meta:
        model = Code

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    class Meta:
        model = Comment
