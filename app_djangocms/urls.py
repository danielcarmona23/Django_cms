from django.urls import path


from .views import *

app_name = 'app_djangocms'

urlpatterns = [
 path('alojamiento', alojamiento, name='alojamiento'),	
 path('inicio', inicio, name='inicio'),	
 path('equipo', equipo, name='equipo'),	
 path('contacto', contacto, name='contacto'),	
 path('hotel_tegu', hotel_tegu, name='hotel_tegu'),
  path('registrar_comentario', registrar_comentario, name='registrar_comentario'),
 ]