from django.urls import path
from tienda import views


urlpatterns = [
    path('inicio/',views.home, name="Home"),
]
