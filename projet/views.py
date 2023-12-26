from rest_framework import viewsets, status

from account.models import Contributor, CustomUser
from projet.models import Project, Issue, Comment
from projet.serializers import ProjectSerializers, IssueSerializers, CommentSerializers

from rest_framework.response import Response


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers

    # Ces deux lignes sont pareilles que rest settings mais pour gérer chaque vue
    # Si utilisation du token de django Rest.
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # contributor = Contributor.objects.create(user=request.user, project=project.id)
        # contributor.save()

        # request.POST._mutable = True
        # request.data['author'] = request.user.id

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        project = serializer.save()

        # Once the project is created, I can assign the correct author
        project.author = CustomUser.objects.get(id=request.user.id)
        project.save()

        projet = Project.objects.get(id=serializer.data['id'])
        Contributor.objects.create(user=request.user, project=projet)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # Méthode qui permet de filtrer les projets qui ont été par leur utilisateurs.
    def get_queryset(self):
        # A ENLEVER SI UTILISATION TOKEN
        if type(self.request.user) == CustomUser:
            queryset = Project.objects.filter(author=self.request.user)
            return queryset
        else:
            return None

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.author:
            self.perform_destroy(instance)
            return Response({'message': "Votre projet a bien été supprimé."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "Vous n'avez pas le droit."}, status=status.HTTP_403_FORBIDDEN)


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializers

    # Méthode qui permet de filtrer les projets qui ont été par leur utilisateurs.
    def get_queryset(self):
        if type(self.request.user) == CustomUser:
            user_contributors = Contributor.objects.filter(user=self.request.user)
            contributed_projects = []
            for contributor in user_contributors:
                contributed_projects.append(contributor.project)
            allowed_issues = Issue.objects.filter(project__in=contributed_projects)
            return allowed_issues
        else:
            return None

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        id_project = request.data.get('project')
        project = Project.objects.get(id=int(id_project))
        if request.user == project.author or len(Contributor.objects.filter(project=project, user=request.user)) != 0:

            self.perform_create(serializer)
            issue = serializer.save()

            # Once the project is created, I can assign the correct author
            issue.author = CustomUser.objects.get(id=request.user.id)
            issue.save()

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'message': "Vous n'avez pas la permission."}, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        if request.user == instance.author:
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': "Vous n'avez pas la permission."}, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.author:
            self.perform_destroy(instance)
            return Response({'message': "Votre problème a bien été supprimé."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "Vous n'avez pas le droit."}, status=status.HTTP_403_FORBIDDEN)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

    # Méthode qui permet de filtrer les comment qui ont été par leur utilisateurs.
    def get_queryset(self):
        if type(self.request.user) == CustomUser:
            user_contributors = Contributor.objects.filter(user=self.request.user)
            contributed_projects = []
            for contributor in user_contributors:
                contributed_projects.append(contributor.project)
            allowed_issues = Issue.objects.filter(project__in=contributed_projects)
            allowed_comments = Comment.objects.filter(issue__in=allowed_issues)
            return allowed_comments
        else:
            return None

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.author:
            self.perform_destroy(instance)
            return Response({'message': "Votre commentaire a bien été supprimé."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': "Vous n'avez pas le droit."}, status=status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        id_issue = request.data.get('issue')
        issue = Issue.objects.get(id=int(id_issue))
        project = issue.project
        if request.user == project.author or len(Contributor.objects.filter(project=project, user=request.user)) != 0:

            self.perform_create(serializer)
            comment = serializer.save()

            # Once the project is created, I can assign the correct author
            comment.author = CustomUser.objects.get(id=request.user.id)
            comment.save()

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'message': "Vous n'avez pas la permission."}, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        if request.user == instance.author:
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': "Vous n'avez pas la permission."}, status=status.HTTP_403_FORBIDDEN)
