from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import *
from rest_framework import serializers

class CustomUserUserSerializer(WritableNestedModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "last_login",
            "onboarded",
            "password",
            "image",
            "sex",
            "address",
            "image_path",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "id": {"read_only": True, "required": False},
        }

    def get_image(self, obj):
        try:
            if obj.image_path:
                return obj.image_path.url
        except Exception:
            return None

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):  #
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)
    

class ShareholderSerializer(WritableNestedModelSerializer):
    user = CustomUserUserSerializer(partial=True)

    class Meta:
        model = Shareholder
        fields = "__all__"



    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        for key, value in user_data.items():
            setattr(instance.user, key, value)
        instance.user.save()
        instance.save()
        return super().update(instance, validated_data)


class ShareholderListSerializer(WritableNestedModelSerializer):
    user = CustomUserUserSerializer(partial=True)

    class Meta:
        model = Shareholder
        fields = "__all__"

class InvestorSerializer(WritableNestedModelSerializer):
    user = CustomUserUserSerializer(partial=True)

    class Meta:
        model = Investor
        fields = "__all__"



    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        for key, value in user_data.items():
            setattr(instance.user, key, value)
        instance.user.save()
        instance.save()
        return super().update(instance, validated_data)


class InvestorListSerializer(WritableNestedModelSerializer):
    user = CustomUserUserSerializer(partial=True)

    class Meta:
        model = Investor
        fields = "__all__"



class FounderSerializer(WritableNestedModelSerializer):
    user = CustomUserUserSerializer(partial=True)

    class Meta:
        model = Founder
        fields = "__all__"

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        for key, value in user_data.items():
            setattr(instance.user, key, value)
        instance.user.save()
        instance.save()
        return super().update(instance, validated_data)


class FounderListSerializer(WritableNestedModelSerializer):
    user = CustomUserUserSerializer(partial=True)

    class Meta:
        model = Founder
        fields = "__all__"

class AdvisorSerializer(WritableNestedModelSerializer):
    user = CustomUserUserSerializer(partial=True)

    class Meta:
        model = Advisor
        fields = "__all__"



    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        for key, value in user_data.items():
            setattr(instance.user, key, value)
        instance.user.save()
        instance.save()
        return super().update(instance, validated_data)


class AdvisorListSerializer(WritableNestedModelSerializer):
    user = CustomUserUserSerializer(partial=True)

    class Meta:
        model = Shareholder
        fields = "__all__"