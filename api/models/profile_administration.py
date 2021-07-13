from django.db import models

from api.models.profile import Profile


class ProfileAdministration(models.Model):
    class Meta:
        db_table = "profile_administration"

    administration_profile = models.ForeignKey(
        Profile, null=False, on_delete=models.CASCADE, related_name="administration_profile"
    )
    administred_profile = models.ForeignKey(
        Profile, null=False, on_delete=models.CASCADE, related_name="administred_profile"
    )

