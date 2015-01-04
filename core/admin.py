from django.contrib import admin
from core.models import Task, TaskEvent, Category, FollowUp
# Register your models here.


admin.site.register(Task)
admin.site.register(TaskEvent)
admin.site.register(Category)
admin.site.register(FollowUp)
