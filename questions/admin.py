from django.contrib import admin
from .models import *
# Register your models here.
class questionAnswer(admin.TabularInline):
    model=ANSWER
class addQA(admin.ModelAdmin):
    inlines=[questionAnswer]
admin.site.register(QUESTION,addQA)