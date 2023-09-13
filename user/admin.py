from django.contrib import admin
from .models import User, Manager, Agent


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_manager', 'is_agent', 'date_joined')


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user',)


# admin.site.register(User)
# admin.site.register(Manager)
admin.site.register(Agent)
