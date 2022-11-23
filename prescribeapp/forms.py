from django import forms
from prescribeapp.models import Review,Prescription,Permission,MedicaleRocord,MedicalTestReport

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review',)

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['test','disease','prescrb','Advice','prescrb_img',]


class MedicaleRocordForm(forms.ModelForm):
    class Meta:
        model = MedicaleRocord
        fields = ['title','record','Advice','record_img',]

class MedicalTestReportForm(forms.ModelForm):
    class Meta:
        model = MedicalTestReport
        fields = ['title','doctor','report','Advice','report_img',]

