from copy import deepcopy
from rest_framework import serializers
from api.models.profile import Profile
from api.models.company import Company
from api.models.profile_administration import ProfileAdministration


from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

User._meta.get_field("email")._unique = True


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "password",
            "username",
            "email",
        )
        extra_kwargs = {
            "email": {"required": True},
        }


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    company = CompanySerializer(required=False)

    class Meta:
        model = Profile
        fields = "__all__"

    def _create_plataform_user(self, validated_data):
        company = None
        if validated_data.get("company"):
            company = validated_data.pop("company")
            company, _ = Company.objects.get_or_create(**company)
        if validated_data.get("user"):
            user = validated_data.pop("user")
            user["password"] = make_password(user["password"])
            user = User.objects.create(**user)
        profile = Profile.objects.create(**validated_data, company=company, user=user)
        ProfileAdministration.objects.create(administration_profile=profile, administred_profile=profile)

    def _create_simple_customer(self, validated_data):
        company = None
        user = None
        profile = Profile.objects.create(**validated_data, company=company, user=user)
        administration_profile = Profile.objects.filter(user_id=self.context["request"].user.id).first()
        ProfileAdministration.objects.create(
            administration_profile=administration_profile, administred_profile=profile
        )

    def create(self, validated_data):
        initial_validated_data = deepcopy(validated_data)
        profile_type_create_mapper = {
            "plataform_user": self._create_plataform_user,
            "simple_customer": self._create_simple_customer,
        }
        profile_type_create_mapper[validated_data["profile_type"]](validated_data)
        return initial_validated_data

    def _validate_plataform_user(self, data):
        if "user" not in data.keys():
            raise serializers.ValidationError(
                {
                    "user": """Para perfis do tipo 'Usuário de plataforma' deve ser informado o usuário a ser criado"""
                }
            )

    def _validade_simple_customer(self, data):
        if "user" in data.keys():
            raise serializers.ValidationError(
                {"user": """Para perfis do tipo 'Cliente simples' não deve ser informado o usuário"""}
            )
        if "company" in data.keys():
            raise serializers.ValidationError(
                {"user": """Para perfis do tipo 'Cliente simples' não deve ser informada a organização"""}
            )

    def validate(self, data):
        profile_type_validate_mapper = {
            "plataform_user": self._validate_plataform_user,
            "simple_customer": self._validade_simple_customer,
        }

        profile_type_validate_mapper[data["profile_type"]](data)
        return data
