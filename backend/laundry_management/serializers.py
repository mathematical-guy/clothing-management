from django.utils import timezone

from .models import LaundryEvent, LaundryCloth
from rest_framework import serializers

class LaundryEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaundryEvent
        fields = "__all__"




class LaundryEventClothListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaundryCloth
        fields = "__all__"

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class AddLaundryClothSerializer(serializers.ModelSerializer):
    name = serializers.CharField(allow_null=True, allow_blank=True)
    description = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    laundry = serializers.PrimaryKeyRelatedField(queryset=LaundryEvent.objects.all())
    image = serializers.ImageField()
    is_ready = serializers.BooleanField(read_only=True)

    class Meta:
        model = LaundryCloth
        fields = (
            "id",
            "name",
            "laundry",
            "description",
            "image",
            "is_ready"
        )


class MarkClothReadySerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    laundry = serializers.CharField(read_only=True)
    image = serializers.CharField(read_only=True)
    is_ready = serializers.CharField(read_only=True)

    class Meta:
        model = LaundryCloth
        fields = (
            "id", "name", "laundry", "description", "image", "is_ready"
        )

    def create(self, validated_data):
        pass

    def validate(self, attrs):
        cloth: LaundryCloth = self.instance
        if cloth is None:
            raise serializers.ValidationError({"id": "Invalid ID"})

        if cloth.is_ready:
            raise serializers.ValidationError({"id": "Cloth is already ready"})

        return super().validate(attrs=attrs)

    def update(self, instance: LaundryCloth, validated_data: dict):
        instance.is_ready = True
        instance.ready_on = timezone.now()
        instance.save()
        return instance
