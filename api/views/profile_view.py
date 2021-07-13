from api.permissions import IsPostOrIsAuthenticated, IsAuthenticatedIfProfileSimpleCustomer
from rest_framework.viewsets import ModelViewSet
from api.models.profile import Profile
from api.models.profile_administration import ProfileAdministration
from api.serializers.profile_serializer import ProfileSerializer


class ProfileView(ModelViewSet):
    permission_classes = (IsPostOrIsAuthenticated, IsAuthenticatedIfProfileSimpleCustomer)
    serializer_class = ProfileSerializer

    def get_queryset(self):
        profile = Profile.objects.get(user_id=self.request.user.id)
        administred_profiles = ProfileAdministration.objects.filter(administration_profile=profile).all()
        return Profile.objects.filter(id__in=[x.administred_profile.id for x in administred_profiles])

