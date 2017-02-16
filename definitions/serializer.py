from rest_framework import serializers
from .models import Words

class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = ('id','word', 'type', 'definition', 'frequency')