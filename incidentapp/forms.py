from django import forms
from incidentapp.models import incident, component

class IncidentForm(forms.ModelForm):
    class Meta:
        model = incident
        fields = ('component', 'name', 'message', 'status', 'notifications')
        
class ComponentForm(forms.ModelForm):
    class Meta:
        model = component
        fields = ('name', 'description')