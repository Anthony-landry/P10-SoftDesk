from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account.views import UserRegistationAPIView, ContributorViewSet

router = DefaultRouter(trailing_slash=True)
router.register("contributors", ContributorViewSet, basename="contributors")

urlpatterns = [

    path('signup/', UserRegistationAPIView.as_view(), name='signup'),
    path('', include(router.urls))

]
