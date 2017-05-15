from rest_framework import serializers
from .models import Stats

class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = ('id','season', 'date', 'player', 'games','pa', 'ab', 'bb', 'so','hidp', 'cs', 'dbo', 'sb',
                  'h', 'firstb', 'secondb', 'thirdb','fourthb', 'hr', 'r', 'rbi')

