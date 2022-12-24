from django.db import models

# Create your models here.
class component(models.Model):
    name = models.CharField(max_length=30, verbose_name='Aplikācijas nosaukums')
    description = models.TextField(verbose_name='Apraksts')
    date = models.DateField(auto_now_add=True, blank=True, verbose_name='Datums')
    time = models.TimeField(auto_now_add=True, blank=True, verbose_name='Laiks')
    
    class Meta:
        verbose_name='Aplikācija'
        verbose_name_plural='Aplikācijas'
    
    def __str__(self):
        return self.name
    
class incident(models.Model):
    component = models.ForeignKey(component, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Temats')
    message = models.TextField(verbose_name='Paziņojums')
    status = models.PositiveIntegerField()
    notifications = models.BooleanField(default=False, verbose_name='Send notifications')
    
    class Meta:
        verbose_name='Incidents'
        verbose_name_plural='Incidents'
        ordering=['name']
    
    def __str__(self):
        return self.name
    
    class company(models.Model):
        name = models.CharField(max_length=30, verbose_name='Nosaukums')
        description = models.TextField(verbose_name='Apraksts')
        email = models.EmailField(max_length = 254, verbose_name='E-pasts')
        component = models.ForeignKey(component, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    