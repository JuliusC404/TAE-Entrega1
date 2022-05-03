from django.shortcuts import redirect, render
from pathlib import Path
from proyect.mayores import prediccionsatisfaccion
from proyect.menores import prediccionsatisfaccionMen

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
    prediction = "No sirvió :("
    if request.GET:
        sexo = request.GET.get('sexo', '')
        anios = request.GET.get('anios', '')
        ingreso = request.GET.get('ingreso', '')
        salud = request.GET.get('salud', '')
        seguridad = request.GET.get('seguridad', '')
        trabajo = request.GET.get('trabajo', '')
        libre = request.GET.get('libre', '')
        feliz = request.GET.get('feliz', '')
        preocupado = request.GET.get('preocupado', '')
        triste = request.GET.get('triste', '')
        worth = request.GET.get('worth', '')
        vida = request.GET.get('vida', '')

        dic = {
            'P6020':[int(sexo)],
            'P6040':[int(anios)],
            'P1896':[int(ingreso)],
            'P1897':[int(salud)],
            'P1898':[int(seguridad)],
            'P1899':[int(trabajo)],
            'P3175':[int(libre)],
            'P1901':[int(feliz)],
            'P1903':[int(preocupado)],
            'P1904':[int(triste)],
            'P1905':[int(worth)],
            'P1927':[int(vida)]
        }
        prediction = prediccionsatisfaccion(dic)
    
    return redirect('../index/prediccion2/'+str(prediction)+'/')


def predictNinios(request):
    prediction = "No sirvió :("
    if request.GET:
        cuidador = request.GET.get('cuidador', '')
        leer = request.GET.get('leer', '')
        jugar = request.GET.get('jugar', '')
        salir = request.GET.get('salir', '')
        vertv = request.GET.get('vertv', '')
        deporte = request.GET.get('deporte', '')
        dispositivos = request.GET.get('dispositivos', '')

        prediction = prediccionsatisfaccionMen([[int(cuidador), int(leer), int(jugar), int(salir), int(vertv), int(deporte), int(dispositivos)]])
    
    return redirect('../index/prediccion1/'+str(prediction)+'/')
