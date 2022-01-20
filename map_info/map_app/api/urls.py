from django.urls import path
from map_app.api.views import ParkInfoCreateAPIView, ParkInfoDetailAPIview, PositionsCreateAPIView

urlpatterns = [
    path('parks/', ParkInfoCreateAPIView.as_view(), name='park-list'),
    path('positions/', PositionsCreateAPIView.as_view(), name='position-list'),
    path('parks/<int:pk>/', ParkInfoDetailAPIview.as_view(), name='park-detail')
]