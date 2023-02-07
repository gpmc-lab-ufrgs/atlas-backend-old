from rest_framework_gis import serializers

from .models import District

class DistrictSerializer(serializers.GeoFeatureModelSerializer):    
    
    class Meta:
        model = District
        geo_field = 'geometry'
        fields = [
            "MUNICIPALITY_CODE",
            "MUNICIPALITY_NAME",
            "ACRONYM_FU",
            "AREA_KM2",
        ]