from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer



from rest_framework import serializers
from .models import Domain, Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class DomainSerializer(WritableNestedModelSerializer):
    tenant = ClientSerializer()

    class Meta:
        model = Domain
        fields = '__all__'

    def create(self, validated_data):
        tenant_data = validated_data.pop('tenant')
        tenant, created = Client.objects.get_or_create(**tenant_data)
        domain = Domain.objects.create(**validated_data, tenant=tenant)
        return domain

    def update(self, instance, validated_data):
        client_data = validated_data.pop('tenant')
        client = instance.client

        instance.name = validated_data.get('name', instance.name)
        instance.save()

        client.name = client_data.get('name', client.name)
        client.save()

        return instance


