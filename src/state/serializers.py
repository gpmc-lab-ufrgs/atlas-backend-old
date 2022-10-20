from rest_framework_gis import serializers


from .models import State

class StateSerializer(serializers.GeoFeatureModelSerializer):
    
    class Meta:
        model = State
        geo_field = 'geometry'
        fields = [
            "CD_UF",
            "POPULATION",
            "NM_UF",
            "SIGLA_UF",
            "NM_REGIAO"
        ]
