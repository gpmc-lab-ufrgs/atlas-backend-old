from rest_framework import serializers

from district_property.serializers import DistrictPropertiesSerializer

from .models import District

class DistrictSerializer(serializers.ModelSerializer):
    properties =  DistrictPropertiesSerializer(read_only=True)
    
    class Meta:
        model = District
        fields = [
            "type",
            "geometry",
            "properties",
        ]