from django.contrib import admin

from projet.models import Project, Issue, Comment

# Register your models here.

admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Comment)
