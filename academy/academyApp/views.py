from tkinter import Entry

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from academyApp.models import Academia
from django.urls import reverse
# Create your views here.


def filtro(request):
    queryset = request.GET.get("drop1")
    cityobj = Academia.objects.filter(city__exact=queryset)
    return render(request,'academies_details2.html',{"latest_academies_list":cityobj})
"""
def displaycity(request):
    cityobj=Academia.objects.values('city').distinct()
    return render(request,'academies_list.html',{"latest_academies_list":cityobj})
"""
"""
def searchAcademy(request, pk):
    academia = get_object_or_404(Academia, pk=pk)
    review = Academia(city=request.POST['city'])
    review.save()
    return HttpResponseRedirect(reverse('academies_details', args=(academia.id,)))
"""

def test(request):
    if request.method == ["GET"]:
        response = request.GET['drop1']
        return render('academies_list.html',{"city":response})
    else:
        return HttpResponse('<h1>Page was found</h1>')



"""if request.method == "POST":
        response = ''
        for key, value in request.POST.items():
            response += '%s \n' % (value)
    return HttpResponse(response)"""
