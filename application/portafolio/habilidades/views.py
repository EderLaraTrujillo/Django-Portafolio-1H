from django.shortcuts import render, HttpResponse # Para vistas basadas en funciones se utiliza este elemento
from django.views.generic import TemplateView # Vistas basadas en clases:

# Create your views here.
class HomeViewPage(TemplateView):
    # Sobreescribimos la variable para indicar cual archivo html renderizar:
    template_name = 'inicio.html'

    # Crear una funcion para mostrar la info de la vista:
    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name, {
            'titulo':'Portafolios',
            'mensaje':'Ten acceso a los perfiles, mas solicitados y preparados del momento.',
            'pregunta': '¿Qué esperas para empezar?',
            'boton': 'Registrate!'
        })



