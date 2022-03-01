from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='entry-point'),
    path('park/<int:id>', views.IndexView.as_view()),
    path('info/', views.IndexView.as_view()),
]