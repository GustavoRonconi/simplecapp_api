from django.urls import path, include

from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

from api.views.profile_view import ProfileView

router = routers.DefaultRouter()
router.register(r"profile", ProfileView, basename="profile")

urlpatterns = [
    path("auth/login/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh",),
    path("", include(router.urls)),
]

