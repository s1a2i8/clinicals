from django.db import models

# Create your models here.
class Patient(models.Model):
    LastName = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=20)
    Age = models.IntegerField()

class ClincalData(models.Model):
    COMPONENT_NAMES = [('hw','Height/weight'),('bp','Blood Pressure'),('heartrate','Heart Rate')]
    ComponentName = models.CharField(choices=COMPONENT_NAMES,max_length=20)
    ComponentValue = models.CharField(max_length=20)
    MeasuredDateTime = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)

    
    

