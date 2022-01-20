from rest_framework import serializers
from map_app.models import ParkInfo, Positions

class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = "__all__"

class ParkInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkInfo
        fields = "__all__"