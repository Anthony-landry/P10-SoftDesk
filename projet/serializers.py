from rest_framework import serializers
from projet.models import Project, Issue, Comment


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        # fields = "__all__"
        # Exclure le champ auteur pour ne pas le rendre sélectionnable dans l'interface DRF
        exclude = ("author",)


class IssueSerializers(serializers.ModelSerializer):
    class Meta:
        model = Issue
        exclude = ("author",)


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ("author",)
