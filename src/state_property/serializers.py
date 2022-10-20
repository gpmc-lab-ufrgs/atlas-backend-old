from rest_framework import serializers

from .models import StateProperty

class StatePropertiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = StateProperty
        fields = [
            "CD_UF",
            "POPULATION",
            "NM_UF",
            "SIGLA_UF",
            "NM_REGIAO",
        ]