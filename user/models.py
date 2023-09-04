from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


# Create your models here.

class User(AbstractUser):
    is_manager = models.BooleanField(_("Manager Status"), default=False)
    is_agent = models.BooleanField(_("Agent Status"), default=False)


class Manager(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True, related_name='manager')

    def __str__(self):
        return str(self.user)


class Agent(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True, related_name='agent')
    manage = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='agent')
    code = models.CharField(_("code"), max_length=6, unique=True)

    def __str__(self):
        return str(self.user)
