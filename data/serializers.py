from rest_framework import serializers

from .models import Data_state

from dictionary.serializers import DictionarySerializer


class DataSerializer(serializers.ModelSerializer):
    dictionary = DictionarySerializer(read_only=True)

    class Meta:
        model = Data_state
        fields = [
            "state",
            "dictionary",
            "value"
        ]