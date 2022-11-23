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
def doc_profile(request, username):
    result_user = User.objects.get(username=username)
    reviews = Review.objects.filter(receiver__username=username)
    review_form = ReviewForm()
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.giver = request.user
            review.receiver = result_user
            review.save()
            return HttpResponseRedirect(reverse('Accountapp:doc_profile' , kwargs={'username':username}))
    return render(request, 'Profile/doctor_profile.html', context={'result_user':result_user, 'review_form':review_form}) 