from rest_framework import permissions

from projet.models import Project


class IsProjectOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        id_project = request.data.get('project')
        if id_project != None:
            project = Project.objects.get(id=int(id_project))
            if request.user == project.author:
                return True
            return False
        return False
