from .models import Universo

def registrar_nuevo_uni(self, **params_nuevouni):
    uninuevo = Universo.objects.all()
    
    nuevouni = Universo.objects.create(
        nombre = params_nuevouni['nombre'],
        user = params_nuevouni['user']
    )
    nuevouni.save()
    return nuevouni