from django.http import HttpResponse
from appcoder.models import Curso



def listado_cursos(request):
    cursos = Curso.objects.all()

    # Respuesta casera
    cadena_respuesta = "<ul>"
    for curso in cursos:
        cadena_respuesta += f"<li>({curso.nombre},{curso.camada}) </li>"
    cadena_respuesta += "</ul>"

    return HttpResponse(cadena_respuesta)
