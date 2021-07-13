import uuid
from django.db import models
from django.contrib.auth.models import User
from api.constants import ProfileTypes, States

from api.models.company import Company


class Profile(models.Model):
    class Meta:
        db_table = "profile"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE, null=True)
    company = models.OneToOneField(Company, related_name="profile", on_delete=models.CASCADE, null=True)
    profile_type = models.CharField(choices=ProfileTypes.choices, max_length=20)

    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=50, unique=True)
    cpf = models.CharField(max_length=50, unique=True)
    state = models.CharField(choices=States.choices, max_length=20)
    cep = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
