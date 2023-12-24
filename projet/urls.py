from django.urls import path, include
from rest_framework.routers import DefaultRouter

from projet.views import ProjectViewSet, IssueViewSet, CommentViewSet

router = DefaultRouter(trailing_slash=True)
router.register("projet", ProjectViewSet, basename="projects")
router.register("issue", IssueViewSet, basename="issues")
router.register("comment", CommentViewSet, basename="comments")


urlpatterns = [

    path('api/', include(router.urls)),

]
