from django.contrib import admin
from .models import User, WeekDay, Lesson, HomeTask, Note
# Register your models here.
admin.site.register(User)
admin.site.register(WeekDay)
admin.site.register(Lesson)
admin.site.register(HomeTask)
admin.site.register(Note)
