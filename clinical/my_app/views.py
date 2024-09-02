from django.shortcuts import render,redirect
from my_app.models import Patient,ClincalData
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from my_app.forms import ClincalDataForm
# Create your views here.

class PatientListView(ListView):
    model = Patient

class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('FirstName','LastName','Age')
class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('FirstName','LastName','Age')
class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')

def addData(request,**kwargs):
    form = ClincalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClincalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'my_app/clinicaldata_forms.html',{'form':form,'patient':patient})
def analyzedata(request,**kwargs):
    data = ClincalData.objects.filter(patient_id=kwargs['pk'])
    responseData = []
    for eachentry in data:
        if eachentry.ComponentName == 'hw':
            heightandweight = eachentry.ComponentValue.split('/')
            if len(heightandweight) > 1 :
                feettometers = float(heightandweight[0]) * 0.4536
                BMI = (float(heightandweight[1]))/feettometers*feettometers
                BMIEntry = ClincalData()
                BMIEntry.ComponentName = 'BMI'
                BMIEntry.ComponentValue = BMI
                responseData.append(BMIEntry)
        responseData.append(eachentry)
    return render(request,'my_app/generateReport.html',{'data':responseData})



