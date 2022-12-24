from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from incidentapp.models import incident, component
from incidentapp.forms import IncidentForm, ComponentForm

# Create your views here.
def home(request):
    return redirect(incidentapp_home)

@login_required(login_url='/incidentapp/sign-in/')
def incidentapp_home(request):
    incidents = incident.objects.all()
    return render(request, 'incidentapp/home.html', {'incidents':incidents})

@login_required(login_url='/incidentapp/sign-in/')
def incidentapp_add_incident(request):
    form = IncidentForm()
    
    if request.method == "POST":
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            incident = form.save(commit=False)
            # incident.incidentapp = request.user.incidentapp
            incident.save()
            return redirect(incidentapp_home)
    
    return render(request, 'incidentapp/add_incident.html', { 'form': form})

def incident_detail(request, incident_id):
    incidentd = get_object_or_404(incident, id=incident_id)
    return render(request, 'incidentapp/incident_detail.html', {'incident':incidentd})

def incidentapp_component(request):
    components = component.objects.all()
    return render(request, 'incidentapp/component.html', {'component': components})

@login_required(login_url='/incidentapp/sign-in/')
def incidentapp_add_component(request):
    form = ComponentForm()
    
    if request.method == "POST":
        form = ComponentForm(request.POST, request.FILES)
        if form.is_valid():
            component = form.save(commit=False)
            # incident.incidentapp = request.user.incidentapp
            component.save()
            return redirect(incidentapp_home)
    
    return render(request, 'incidentapp/add_component.html', { 'form': form})

@login_required(login_url='/incidentapp/sign-in/')
def incidentapp_status(request):
    incidentStatus = incident.objects.all()
    return render(request, 'incidentapp/status.html', {'incident': incidentStatus})
