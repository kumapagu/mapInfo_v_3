from rest_framework import serializers
from map_app.models import ParkInfo

class ParkInfoSerializer(serializers.ModelSerializer):
    # position = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ParkInfo
        fields = "__all__"