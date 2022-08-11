from django.shortcuts import render
from django.db import transaction,connections
from django.http import HttpResponseRedirect,JsonResponse, HttpResponse
from django.urls import reverse
from app_djangocms.models import Comentario

# Create your views here.
def alojamiento(request):
    
    return render(request, 'Alojamientos.html')


def inicio(request):
    
    return render(request, 'inicio.html')
    

def equipo(request):
    
    return render(request, 'team.html')

def contacto(request):
    
    return render(request, 'contacto.html')

def hotel_tegu(request):
    
    return render(request, 'hotel_tegu.html')


def registrar_comentario(request):
    ctx={}
    ret_data,query_comentario,errores = {},{},{}
    comentarios = Comentario.objects.all()
    

    if request.method == 'POST':
    
        ret_data['nombre'] = request.POST.get('nombre')
        ret_data['correo'] = request.POST.get('correo')
        ret_data['asunto'] = request.POST.get('asunto')
        ret_data['comentario'] = request.POST.get('comentario')
    

        # Nombres
        if request.POST.get('nombre') == '':
            errores['nombre'] = "Debe ingresar el nombre"
        else:
            query_comentario["nombre"] = request.POST.get('nombre')

        
        # Correo
        if request.POST.get('correo') == '':
            errores['correo'] = "Debe ingresar el correo"
            
        else:
            query_comentario["correo"] = request.POST.get('correo')

        # Asunto
        if request.POST.get('asunto') == '':
            errores['asunto'] = "Debe ingresar el asunto"
            
        else:
            query_comentario["asunto"] = request.POST.get('asunto')
            
        # Comentario
        if request.POST.get('comentario') == '':
            errores['comentario'] = "Debe ingresar el asunto"
            
        else:
            query_comentario["comentario"] = request.POST.get('comentario')
    
        print(errores)
        if not errores:

            try:
                coment = Comentario(**query_comentario)
                print(query_comentario)
                coment.save()

            except Exception as e:
                transaction.rollback()
                errores['administrador'] = e
                print (e)
                ctx = {'comentarios':comentarios,'errores':errores,'ret_data':ret_data }
        else:
                transaction.commit()
                return HttpResponseRedirect(reverse('app_djangocms:registrar_comentario')+'?ok')
    else:
        ctx = {'comentarios':comentarios,'errores':errores,'ret_data':ret_data }
        return render(request,'contacto.html',ctx)
        
    return render(request,'contacto.html',ctx)	 
