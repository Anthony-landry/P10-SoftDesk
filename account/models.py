from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from projet.models import Project
from softdesk import settings


class CustomUserManager(BaseUserManager):

    def create_user(self, password, age, can_be_contacted, can_data_be_shared, **kwargs):
        user = self.model(age=age, can_be_contacted=can_be_contacted,
                          can_data_be_shared=can_data_be_shared, **kwargs)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, age, can_be_contacted, can_data_be_shared, password, **kwargs):
        kwargs["is_staff"] = True
        kwargs["is_superuser"] = True
        kwargs["is_active"] = True

        return self.create_user(password=password, age=age, can_be_contacted=can_be_contacted,
                                can_data_be_shared=can_data_be_shared, **kwargs)


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField()
    can_be_contacted = models.BooleanField()
    can_data_be_shared = models.BooleanField()

    objects = CustomUserManager()

    REQUIRED_FIELDS = ["age", "can_be_contacted", "can_data_be_shared"]


class Contributor(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user',
        related_query_name='user'
    )
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name='project_contributors',
        related_query_name='project_contributors'
    )

    # permission = serializers.ChoiceField(choices=[('1', 'all'), ('2', 'none')])
    # role = models.CharField(max_length=128, default='contributor')

    def __str__(self):
        return f"Contributor {self.user.username}"
