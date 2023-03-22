from rest_framework_gis import serializers

from .models import District

class DistrictSerializer(serializers.GeoFeatureModelSerializer):    
    
    class Meta:
        model = District
        geo_field = 'geometry'
        fields = [
            "CD_MUN",
            "NM_MUN",
            "SIGLA_UF",
            "AREA_KM2",
        ]