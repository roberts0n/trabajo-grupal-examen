from django.urls import path
from tienda import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('inicio/',views.home, name="Home"),
    path('detalle/<int:juego_id>/',views.detalleJuego, name='detalle_juego')
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)