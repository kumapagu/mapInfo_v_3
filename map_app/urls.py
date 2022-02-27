from django.urls import re_path, path
from . import views

urlpatterns = [
    # re_path('', views.IndexView.as_view(), name='entry-point'),
    path('', views.IndexView.as_view(), name='entry-point'),
]