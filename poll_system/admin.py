from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(TopicPoll)
admin.site.register(Choice)
admin.site.register(Question)