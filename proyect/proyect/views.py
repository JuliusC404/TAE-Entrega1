from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import redirect, render
from pathlib import Path
from subprocess import check_output, run, Popen, call, PIPE
import os

BASE_DIR = Path(__file__).resolve().parent.parent

""" def index(request):

    dochtml = open("index.html")
    plt = Template(dochtml.read())
    dochtml.close()

    rutashow = 'test/'
    rutacom = os.path.join(BASE_DIR, rutashow)

    context = Context({
        "RutaTest": rutashow
    })
    doc = plt.render(context)
    
    return HttpResponse(doc) """

def index(request):

    """ dochtml = open("index.html")
    plt = Template(dochtml.read())
    dochtml.close() """

    rutashow = 'test/'
    rutacom = os.path.join(BASE_DIR, rutashow)

    context = {
        "RutaTest": rutashow
    }
    """ doc = plt.render(context) """
    
    return render(request, 'index.html', context)


def index2(request, Porta, Ruta):

#Define la ruta actual
    rutashow = ''
    rutasplit = Ruta.split('-')
    for rut in rutasplit:
        rutashow = os.path.join(rutashow, rut)

#Lista las carpetas y archivos
    with os.scandir(rutashow) as items:
        subfolder = [fichero.name for fichero in items if fichero.is_dir()]

    with os.scandir(rutashow) as items:
        archives = [fichero.name for fichero in items if fichero.is_file()]

#Habilita o Desabilita el 'Paste'
    Paste = False
    if Porta[:4]=='Copy' or Porta[:3]=='Cut':
        Paste = True

    context = {
        "RutaTest": Ruta,
        "Porta": Porta,
        "Paste": Paste,
        "subfolder": subfolder,
        "archives": archives
    }
    
    return render(request, 'index2.html', context)

def test(request):
    mensaje = ""

    rutas = ['test']
    
    rutashow= ''
    for rut in rutas:
        rutashow = os.path.join(rutashow,rut)

    with os.scandir(rutashow) as items:
        subfolder = [fichero.name for fichero in items if fichero.is_dir()]

    with os.scandir(rutashow) as items:
        archives = [fichero.name for fichero in items if fichero.is_file()]

    if request.GET:
        if request.GET.get('Tipo', '')!='' and request.GET.get('Nombre', '')!='':
            crear(request, rutashow)
            mensaje = rutashow
    else: 
        mensaje = "No dio :("
    return HttpResponse([subfolder, archives])

#Vista Atras

def atras(request, Porta, Ruta):
    newRuta = ''
    rutasplit = Ruta.split('-')[:-1]
    for i in rutasplit:
        newRuta = newRuta + i + '-'
    return redirect('/index2/' + Porta + '/' + newRuta[:-1])

#Vista Abrir

def abrir(request, Porta, Ruta):
    if request.GET:            
            name = request.GET.get('Name', '')
    return redirect('/index2/' + Porta + '/' + Ruta + '-' + name)

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
    #return HttpResponse(comando)