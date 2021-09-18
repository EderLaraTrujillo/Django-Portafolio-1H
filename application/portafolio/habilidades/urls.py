from django.urls import path
# importamos las vistas de la aplicacion:
from .views import HomeViewPage

# Escribo mis propias rutas:: 
urlpatterns = [
    path('', HomeViewPage.as_view(), name = 'inicio')
]