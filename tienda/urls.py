from django.urls import path
from tienda import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home, name="Home"),
    path('detalle/<int:juego_id>/',views.detalleJuego, name='detalle_juego'),
    path('logout/',views.exit , name="Exit"),
    path('register/',views.register, name="register"),
    path('plataforma/steam',views.categoriaSteam, name="steam"),
    path('plataforma/switch',views.categoriaSwitch, name="switch"),
    path('plataforma/playstation',views.categoriaPlay, name="playstation"),
    path('plataforma/xbox',views.categoriaXbox, name="xbox"),
    path('categoria/rpg',views.categoriaRpg, name="rpg"),
    path('categoria/accion',views.categoriaAccion, name="accion"),
    path('categoria/deportes',views.categoriaDeportes, name="deportes"),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)