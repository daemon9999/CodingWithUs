from django.contrib import admin
from .models import Detail
# Register your models here.


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    class Meta:
        model = Detail
