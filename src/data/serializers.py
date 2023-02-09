from rest_framework import serializers

from dictionary.serializers import DictionarySerializer

from .models import Data


class DataSerializer(serializers.ModelSerializer):    
    dictionary = DictionarySerializer(read_only=True)
    
    class Meta:
        model = Data
        fields = [
            'region_id',
            'name',
            'value',
            'type',
            'dictionary',
        ]