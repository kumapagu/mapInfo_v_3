from django.urls import path
from map_app.api.views import ParkInfoCreateAPIView, ParkInfoDetailAPIview

urlpatterns = [
    path('parks/', ParkInfoCreateAPIView.as_view(), name='park-list'),
    path('parks/<int:pk>/', ParkInfoDetailAPIview.as_view(), name='park-detail')
]