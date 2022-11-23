from django.contrib import admin
from prescribeapp.models import MedicaleRocord,Permission,MedicalTestReport,Likes,Review,Prescription

# Register your models here.
admin.site.register(MedicaleRocord)
admin.site.register(Permission)
admin.site.register(MedicalTestReport)
admin.site.register(Likes)
admin.site.register(Review)
admin.site.register(Prescription)
