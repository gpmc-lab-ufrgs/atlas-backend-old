from rest_framework import serializers

from state_property.serializers import StatePropertiesSerializer

from .models import State

class StateSerializer(serializers.ModelSerializer):
    properties =  StatePropertiesSerializer(read_only=True)
    
    class Meta:
        model = State
        fields = [
            "type",
            "geometry",
            "properties",
        ]