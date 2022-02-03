from rest_framework import generics
from map_app.models import ParkInfo
from map_app.api.permissions import IsAdminUserOrReadOnly
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from map_app.api.serializers import ParkInfoSerializer

class ParkInfoCreateAPIView(generics.ListCreateAPIView):
    queryset = ParkInfo.objects.all().order_by("-id")
    serializer_class = ParkInfoSerializer
    # authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)
    # permission_classes = [IsAdminUserOrReadOnly]

class ParkInfoDetailAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParkInfo.objects.all()
    serializer_class = ParkInfoSerializer
    # permission_classes = [IsAdminUserOrReadOnly]