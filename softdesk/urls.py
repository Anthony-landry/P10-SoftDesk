from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from softdesk.views import index

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # Pour avoir le bouton login sur l'interface Rest
    path('api/account/', include('account.urls')),
    path('', include('projet.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
