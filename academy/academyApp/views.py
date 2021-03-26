from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from academyApp.models import Academia
from django.urls import reverse

# Create your views here.

def displaycity(request):
    cityobj=Academia.objects.values('city').distinct()
    return render(request,'academies_list.html',{"latest_academies_list":cityobj})

def searchAcademy(request, pk):
    academia = get_object_or_404(Academia, pk=pk)
    review = Academia(city=request.POST['city'])
    review.save()
    return HttpResponseRedirect(reverse('academies_details', args=(academia.city,)))
