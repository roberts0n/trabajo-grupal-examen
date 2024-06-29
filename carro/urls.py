from django.urls import path

from carro import views

app_name= "carro"

urlpatterns=[

    path("add/<int:juego_id>/",views.añadirCarrito, name="add"),
    path("remove/<int:juego_id>/",views.añadirCarrito, name="remove"),
    path("decrement/<int:juego_id>/",views.añadirCarrito, name="decrement"),
    path("clean/<int:juego_id>/",views.añadirCarrito, name="clean"),
    path("carrito/",views.verCarrito, name="verCarro"),
]

