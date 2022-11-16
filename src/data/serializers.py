from rest_framework import serializers

from .models import Data

from dictionary.serializers import DictionarySerializer

class DataSerializer(serializers.ModelSerializer):    
    dictionary = DictionarySerializer(read_only=True)
    
    class Meta:
        model = Data
        fields = [
            "region_id",
            "name",
            "value",
            "type",
            "dictionary",
        ]