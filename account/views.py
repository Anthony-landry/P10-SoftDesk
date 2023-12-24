from django.contrib.auth import get_user_model

from rest_framework import generics, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from account.models import Contributor
from account.permissions import IsProjectOwner
from account.serializers import UserRegistrationSerializers, ContributorSerializers
from projet.models import Project

User = get_user_model()


class UserRegistationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializers
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Verifie l'age : RGPD
            if int(serializer.initial_data['age']) < 15:
                return Response({'message': "Vous n'avez pas l'âge"}, status=status.HTTP_403_FORBIDDEN)
            user = serializer.save()

            return Response({'message': f"L'utilisateur (id :{user.id}) a bien été créé"},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorSerializers

    # Les contributeurs sont créés automatiquement et un auteur de projet peut les voir mais c'est tout.
    def get_permissions(self):
        permission_classes = []
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated, ]
        elif self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsProjectOwner, ]
        return [permission() for permission in permission_classes]

    # Seul l'auteur de projet peut voir les contributeurs de son/ses projet(s)
    def get_queryset(self):
        projects = Project.objects.filter(author=self.request.user)
        projects_ids = [project.id for project in projects]
        contributors = Contributor.objects.filter(project__in=projects_ids)
        return contributors

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': "Le contributeur a bien été supprimé."},
                        status=status.HTTP_204_NO_CONTENT)
