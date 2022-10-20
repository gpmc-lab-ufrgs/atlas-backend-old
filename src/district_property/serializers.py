from rest_framework import serializers

from .models import DistrictProperty

class DistrictPropertiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = DistrictProperty
        fields = [
            "CD_MUN",
            "NM_MUN",
            "SIGLA_UF",
            "AREA_KM2",
        ]