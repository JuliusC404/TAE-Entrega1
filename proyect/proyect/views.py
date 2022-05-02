from django.shortcuts import redirect, render
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def rredirect(request):
    return redirect('/index/inicio/-/')

def index(request, current, predict):

    context = {
        "current": current,
        "predict": predict
    }
    
    return render(request, 'Index.html', context)

# Predicción para abuelos
def predictAbue(request):
    comando = "No sirvió :("
    if request.GET:
        sexo = request.GET.get('sexo', '')
        abuelo = request.GET.get('abuelo', '')
        ingreso = request.GET.get('ingreso', '')
        salud = request.GET.get('salud', '')
        seguridad = request.GET.get('seguridad', '')
        trabajo = request.GET.get('trabajo', '')
        feliz = request.GET.get('feliz', '')
        preocupado = request.GET.get('preocupado', '')
        triste = request.GET.get('triste', '')
        worth = request.GET.get('worth', '')
        vida = request.GET.get('vida', '')

        comando = sexo + abuelo + ingreso + salud + seguridad + trabajo + feliz + preocupado + triste + worth + vida
    
    return redirect('../index/inicio/'+comando+'/')
"""
#Vista Crear

def crear(request, Porta, Ruta):

    rutashow = ''
    rutasplit = Ruta.split('-')
    for rut in rutasplit:
        rutashow = os.path.join(rutashow, rut)
        
    if request.GET:
        if request.GET.get('Tipo', '')!='' and request.GET.get('Nombre', '')!='':

            if request.GET.get('Tipo', '')=='Directorio':
                comando = "mkdir %s" % os.path.join(rutashow, request.GET.get('Nombre', ''))
                run(comando, shell=True)
            if request.GET.get('Tipo', '')=='Archivo':
                Nombre = request.GET.get('Nombre', '')
                if '.' not in Nombre:
                    Nombre = Nombre + '.txt'
                comando = "type null > %s" % os.path.join(rutashow, Nombre)
                run(comando, shell=True)

    return redirect('/index2/'+ Porta + '/' + Ruta)

#Vista Cambiar Nombre

def cambiarnombre(request, Porta, Ruta):

    rutashow = ''
    rutasplit = Ruta.split('-')
    for rut in rutasplit:
        rutashow = os.path.join(rutashow, rut)
        
    if request.GET:
        if request.GET.get('Name', '')!='' and request.GET.get('Nuevo', '')!='':

            if request.GET.get('Tipo', '')=='Directorio':
                comando = "ren %s %s" % (os.path.join(rutashow, request.GET.get('Name', '')),request.GET.get('Nuevo', ''))
                run(comando, shell=True)
            if request.GET.get('Tipo', '')=='Archivo':
                Nombre = request.GET.get('Nombre', '')
                if '.' not in Nombre:
                    Nombre = Nombre + '.txt'
                comando = "ren %s %s" % (os.path.join(rutashow, request.GET.get('Name', '')),request.GET.get('Nuevo', ''))
                run(comando, shell=True)

    return redirect('/index2/'+ Porta + '/' + Ruta)

#Vista Eliminar

def eliminar(request, Porta, Ruta):

    rutashow = ''
    rutasplit = Ruta.split('-')
    for rut in rutasplit:
        rutashow = os.path.join(rutashow, rut)
        
    if request.GET:
        if request.GET.get('Name', '')!='':

            if request.GET.get('Tipo', '')=='Directorio':
                comando = "rd /S /Q %s" % os.path.join(rutashow, request.GET.get('Name', ''))
                p = Popen(comando, shell=True)
                p.wait()
            if request.GET.get('Tipo', '')=='Archivo':
                comando = "del %s" % os.path.join(rutashow, request.GET.get('Name', ''))
                p = Popen(comando, shell=True)
                p.wait()

    return redirect('/index2/' + Porta + '/' + Ruta)

#Vista copiar

def copiar(request, Porta, Ruta):

    if request.GET:
        if request.GET.get('Tipo', '')!='' and request.GET.get('Name', '')!='':
            Porta = 'Copy-' + request.GET.get('Tipo', '') + '-' + Ruta + '-' + request.GET.get('Name', '')
    return redirect('/index2/' + Porta + '/' + Ruta)

#Vista cortar

def cortar(request, Porta, Ruta):

    if request.GET:
        if request.GET.get('Tipo', '')!='' and request.GET.get('Name', '')!='':
            Porta = 'Cut-' + request.GET.get('Tipo', '') + '-' + Ruta + '-' + request.GET.get('Name', '')
    return redirect('/index2/' + Porta + '/' + Ruta)

#Vista pegar

def pegar(request, Porta, Ruta):

    ruta2 = ''
    rutasplit = Ruta.split('-')
    for rut in rutasplit:
        ruta2 = os.path.join(ruta2, rut)

    ruta1 = ''
    portasplit = Porta.split('-')
    for i in range(2,len(portasplit)):
        ruta1 = os.path.join(ruta1, portasplit[i])

    comando = ''
    if portasplit[0]=='Copy' and portasplit[1]=='Directorio':
        comando = "xcopy /E /I /C /Y /H %s %s" % (ruta1, os.path.join(ruta2, portasplit[-1]))
        p = Popen(comando, shell=True)
        p.wait()

    elif portasplit[0]=='Copy' and portasplit[1]=='Archivo':
        comando = "copy %s %s" % (ruta1, os.path.join(ruta2,''))
        p = Popen(comando, shell=True)
        p.wait()

    elif portasplit[0]=='Cut' and portasplit[1]=='Directorio':
        comando = "move %s %s" % (ruta1, os.path.join(ruta2, ''))
        p = Popen(comando, shell=True)
        p.wait()
        Porta = 'test'

    elif portasplit[0]=='Cut' and portasplit[1]=='Archivo':
        comando = "move %s %s" % (ruta1, os.path.join(ruta2,''))
        p = Popen(comando, shell=True)
        p.wait()
        Porta = 'test'

    return redirect('/index2/' + Porta + '/' + Ruta)
    #return HttpResponse(comando) """