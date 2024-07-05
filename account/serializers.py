from rest_framework import serializers
from .models import  Investing, Founding, Advising, CustomUser
from drf_writable_nested import WritableNestedModelSerializer


class CustomUserUserSerializer(WritableNestedModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = "__all__"
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

class InvestingSerializer(WritableNestedModelSerializer):
    user = CustomUserUserSerializer(partial=True)

    class Meta:
        model = Investing
        fields = "__all__"

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        for key, value in user_data.items():
            setattr(instance.user, key, value)
        instance.user.save()
        instance.save()
        return super().update(instance, validated_data)

class InvestingListSerializer(serializers.ModelSerializer):
    user = CustomUserUserSerializer(partial=True)

    class Meta:
        model = Investing
        fields = "__all__"

class FoundingSerializer(WritableNestedModelSerializer):
    user = CustomUserUserSerializer(partial=True)

    class Meta:
        model = Founding
        fields = "__all__"

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        for key, value in user_data.items():
            setattr(instance.user, key, value)
        instance.user.save()
        instance.save()
        return super().update(instance, validated_data)

class FoundingListSerializer(serializers.ModelSerializer):
    user = CustomUserUserSerializer(partial=True)

    class Meta:
        model = Founding
        fields = "__all__"

class AdvisingSerializer(WritableNestedModelSerializer):
    user = CustomUserUserSerializer(partial=True)

    class Meta:
        model = Advising
        fields = "__all__"

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        for key, value in user_data.items():
            setattr(instance.user, key, value)
        instance.user.save()
        instance.save()
        return super().update(instance, validated_data)

class AdvisingListSerializer(serializers.ModelSerializer):
    user = CustomUserUserSerializer(partial=True)

    class Meta:
        model = Advising
        fields = "__all__"