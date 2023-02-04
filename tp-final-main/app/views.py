from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import *
from .models import *


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'app/pages/home.html')


def entreprises(request: HttpRequest) -> HttpResponse:
    entreprises = Entreprise.objects.all()
    context = { "entreprises": entreprises }
    return render(request, 'app/pages/entreprises.html', context)


def clients(request: HttpRequest) -> HttpResponse:
    clients = Client.objects.all()
    context = { "clients": clients }
    return render(request, 'app/pages/clients.html', context)


def reclamations(request: HttpRequest) -> HttpResponse:
    reclamations = Reclamation.objects.all()
    context = { "reclamations": reclamations }
    return render(request, 'app/pages/reclamations.html', context)


def entreprise(request: HttpRequest, pk: int) -> HttpResponse:
    entreprise = Entreprise.objects.get(id=pk)
    context = { "entreprise": entreprise }
    return render(request, 'app/pages/entreprise.html', context)


def client(request: HttpRequest, pk: int) -> HttpResponse:
    client = Client.objects.get(id=pk)
    context = { "client": client }
    return render(request, 'app/pages/client.html', context)


def reclamation(request: HttpRequest, pk: int) -> HttpResponse:
    reclamation = Reclamation.objects.get(id=pk)
    context = { "reclamation": reclamation }
    return render(request, 'app/pages/reclamation.html', context)


def create_entreprise(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = EntrepriseForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('entreprises')
    form = EntrepriseForm()
    context = { "form": form }
    return render(request, 'app/pages/create-entreprise.html', context)


def create_client(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('clients')
    form = ClientForm()
    context = { "form": form }
    return render(request, 'app/pages/create-client.html', context)


def create_reclamation(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ReclamationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('reclamations')
    form = ReclamationForm()
    context = { "form": form }
    return render(request, 'app/pages/create-reclamation.html', context)


def update_entreprise(request: HttpRequest, pk: int) -> HttpResponse:
    entreprise = Entreprise.objects.get(id=pk)
    if request.method == "POST":
        form = EntrepriseForm(request.POST, instance=entreprise)
        if form.is_valid:
            form.save()
            return redirect('entreprises')
    form = EntrepriseForm(instance=entreprise)
    context = { "form": form }
    return render(request, 'app/pages/update-entreprise.html', context)


def update_client(request: HttpRequest, pk: int) -> HttpResponse:
    client = Client.objects.get(id=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid:
            form.save()
            return redirect('clients')
    form = ClientForm(instance=client)
    context = { "form": form }
    return render(request, 'app/pages/update-client.html', context)


def update_reclamation(request: HttpRequest, pk: int) -> HttpResponse:
    reclamation = Reclamation.objects.get(id=pk)
    if request.method == "POST":
        form = ReclamationForm(request.POST, instance=reclamation)
        if form.is_valid:
            form.save()
            return redirect('reclamations')
    form = ReclamationForm(instance=reclamation)
    context = { "form": form }
    return render(request, 'app/pages/update-reclamation.html', context)


def delete_entreprise(request: HttpRequest, pk: int) -> HttpResponse:
    entreprise = Entreprise.objects.get(id=pk)
    entreprise.delete()
    return redirect('entreprises')


def delete_client(request: HttpRequest, pk: int) -> HttpResponse:
    client = Client.objects.get(id=pk)
    client.delete()
    return redirect('clients')


def delete_reclamation(request: HttpRequest, pk: int) -> HttpResponse:
    reclamation = Reclamation.objects.get(id=pk)
    reclamation.delete()
    return redirect('reclamations')


def validate_reclamation(request: HttpRequest, pk: int) -> HttpResponse:
    reclamation = Reclamation.objects.get(id=pk)
    reclamation.traite = True
    reclamation.save()
    return redirect('reclamations')


def devalidate_reclamation(request: HttpRequest, pk: int) -> HttpResponse:
    reclamation = Reclamation.objects.get(id=pk)
    reclamation.traite = False
    reclamation.save()
    return redirect('reclamations')