from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest

from academyApp.forms import FormularioAlumno
# Create your views here.

"""
def filtro(request):
    queryset = request.GET.get("drop1")
    cityobj = Academia.objects.filter(city__contains=queryset)
    return render(request,'academies_details2.html',{"latest_academies_list":cityobj})
"""
"""Borrar ciudades repetidas"""
"""
def displaycity(request):
    cityobj=Academia.objects.values('city').distinct()
    return render(request,'academies_list.html',{"latest_academies_list":cityobj})
"""
"""
def filtro(request):
    queryset = request.GET.get("drop1")
    cityobj = Academia.objects.filter(city__contains=queryset)
    return render(request,'academies_details2.html',{"latest_academies_list":cityobj})

def test(request):
    if request.method == ["GET"]:
        response = request.GET['drop1']
        return render('academies_list.html',{"name":response})
    else:
        return HttpResponse('<h1>Page was not found</h1>')

def review(request, pk):
    academia = get_object_or_404(Academia, pk=pk)
    review = AcademiaReview(rating=request.POST['rating'], comment=request.POST['comment'], user=request.user,
        academia=academia)
    review.save()
    return HttpResponseRedirect(reverse('review_create', args=(academia.id,)))
"""
class FormularioAlumnoView(HttpRequest):

    def index(request):
        alumno = FormularioAlumno()
        return render(request, "insert_views.html", {"form":alumno})

    def procesar_formulario(request):
        alumno = FormularioAlumno(request.POST)
        if alumno.is_valid():
            alumno.save()
            alumno = FormularioAlumno()
        return render(request, "insert_views.html", {"form":alumno, "mensaje":'OK'})