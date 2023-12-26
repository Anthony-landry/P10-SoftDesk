import uuid as uuid
from django.db import models
from django.conf import settings


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    type = models.CharField(max_length=128, choices=[('back', 'back-end'), ('front', 'front-end'), ('ios', 'iOS'),
                                                     ('android', 'Android')])
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='project_author',
        related_query_name='project_author',
        null=True
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Projet {self.title}"


class Issue(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    tag = models.CharField(max_length=128, choices=[('bug', 'BUG'), ('feature', 'FEATURE'), ('task', 'TASK')])
    priority = models.CharField(max_length=128, choices=[('low', 'LOW'), ('medium', 'MEDIUM'), ('high', 'HIGH')])
    status = models.CharField(max_length=128, choices=[('to_do', 'To Do'), ('in_progress', ' In Progress'),
                                                       ('finished', 'Finished')], default="to_do")

    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name='issue_project',
        related_query_name='issue_project'
    )
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='issue_author',
        related_query_name='issue_author',
        null=True
    )
    assignee = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='issue_assignee',
        related_query_name='issue_assignee',
        blank=True,
        null=True
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Issue {self.title}"


class Comment(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(max_length=2048)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comment_author',
        related_query_name='comment_author',
        null=True
    )
    issue = models.ForeignKey(
        to=Issue,
        on_delete=models.CASCADE,
        related_name='comment_issue',
        related_query_name='comment_issue'
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.uuid}"
