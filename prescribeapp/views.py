from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from prescribeapp.models import Prescription, MedicaleRocord, MedicalTestReport, Review
from AccountApp.models import User
from prescribeapp.forms import ReviewForm, PrescriptionForm, MedicaleRocordForm, MedicalTestReportForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def patient_profile(request, username):
    result_user = User.objects.get(username=username)
    PresForm =PrescriptionForm()
    if request.method == "POST":
        PresForm = PrescriptionForm(request.POST, request.FILES)
        if PresForm.is_valid():
            prescrip = PresForm.save(commit=False)
            prescrip.doctor = request.user
            prescrip.patient = result_user
            prescrip.save()
            return HttpResponseRedirect(reverse('prescrib:patient_profile'))
     
    MrecordForm =MedicaleRocordForm()
    if request.method == "POST":
        MrecordForm = MedicaleRocordForm(request.POST, request.FILES)
        if MrecordForm.is_valid():
            Mrecord = PresForm.save(commit=False)
            Mrecord.hospital = request.user
            Mrecord.patient = result_user
            Mrecord.save()
            return HttpResponseRedirect(reverse('prescrib:patient_profile'))

    TReportForm =MedicalTestReportForm()
    if request.method == "POST":
        TReportForm = MedicalTestReportForm(request.POST, request.FILES)
        if TReportForm.is_valid():
            TReport = PresForm.save(commit=False)
            TReport.lab = request.user
            TReport.patient = result_user
            TReport.save()
            return HttpResponseRedirect(reverse('prescrib:patient_profile'))
    return render(request, 'Account/patient_profile.html', context={'result_user':result_user, 'PresForm':PresForm,'MrecordForm':MrecordForm,'TReportForm':TReportForm})

@login_required
def Add_to_patientprofile(request, username):
    result_user = User.objects.get(username=username)
    if request.user.is_doctor:
        text= 'Provide prescription'
        Form =PrescriptionForm()
        if request.method == "POST":
            Form = PrescriptionForm(request.POST, request.FILES)
            if Form.is_valid():
                prescrip = Form.save(commit=False)
                prescrip.doctor = request.user
                prescrip.patient = result_user
                prescrip.save()
                return HttpResponseRedirect(reverse('prescrib:patient_profile'))
    if request.user.is_hospital:
        text= 'Provide Medical Record'    
        Form=MedicaleRocordForm()
        if request.method == "POST":
            Form = MedicaleRocordForm(request.POST, request.FILES)
            if Form.is_valid():
                Mrecord = Form.save(commit=False)
                Mrecord.hospital = request.user
                Mrecord.patient = result_user
                Mrecord.save()
                return HttpResponseRedirect(reverse('prescrib:patient_profile'))
    if request.user.is_labratory:
        text= 'Provide Test result'
        Form=MedicalTestReportForm()
        if request.method == "POST":
            Form = MedicalTestReportForm(request.POST, request.FILES)
            if Form.is_valid():
                TReport = Form.save(commit=False)
                TReport.lab = request.user
                TReport.patient = result_user
                TReport.save()
                return HttpResponseRedirect(reverse('prescrib:patient_profile', kwargs={'username':username} ))
    return render(request, 'Add_to_patientprofile.htm', context={'result_user':result_user, 'Form':Form, 'text':text})





