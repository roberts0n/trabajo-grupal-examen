from django.urls import path

from juegos import views

app_name= "juego"

urlpatterns=[

    path("add/",views.add_juego, name="add"),
    path("edit/<int:juego_id>",views.editar_juego, name="edit"),
    path("read/",views.leer_juego, name="read"),
    path("delete/<int:juego_id>",views.delete_juego, name="delete"),
]

