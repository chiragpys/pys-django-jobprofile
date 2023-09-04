from django.contrib import admin
from .models import User, Manager, Agent

# Register your models here.

admin.site.register(User)
admin.site.register(Manager)
admin.site.register(Agent)
