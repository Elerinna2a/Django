from django.urls import path

from .views import formation, formations, home

urlpatterns = [
    path('', home),
    path('formations/', formations),
    path('formations/<int:pk>/', formation),
]
