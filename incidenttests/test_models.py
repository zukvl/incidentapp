from django.test import TestCase
from django.utils import timezone
from incidentapp.models import component

class ComponentTestCase(TestCase):
    def test_string_representation(self):
        comp = component(name="Axapta")
        self.assertEqual(str(comp), comp.name)
    
    def test_verbose_name_plural(self):
        self.assertEqual(str(component._meta.verbose_name_plural), "Aplikācijas")
        
class ComponentFormTest(TestCase):
    def create_compform(self, title="newApp", comments="testApp"):
        return component.objects.create(name=title, description=comments, date=timezone.now(), time =timezone.now())

    def test_compform_creation(self):
        w = self.create_compform()
        self.assertTrue(isinstance(w, component))
        self.assertEqual(w.__str__(), w.name)