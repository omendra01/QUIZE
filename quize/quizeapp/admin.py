from django.contrib import admin

from .models import *

# admin.register(QuizeQuestion)
# class QuizeqouestionAdmin(admin.ModelAdmin):
#     list_display =['question','option1','option2','option3','option4','answer']

@admin.register(QuizeQuestion)
class QuizeAdmin(admin.ModelAdmin):
    list_display = ['question','option1','option2','option3','option4','answer']


@admin.register(Register)
class registerAdmin(admin.ModelAdmin):
    list_display = ['mobile',]