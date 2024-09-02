from django import forms
from my_app.models import ClincalData,Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
class ClincalDataForm(forms.ModelForm):
    class Meta:
        model = ClincalData
        fields = '__all__'
