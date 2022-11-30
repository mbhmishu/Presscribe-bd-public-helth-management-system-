from django.contrib import admin
from .models import User,UserProPic,PatientInfo,DoctorInfo,PharInfo,OrgInfo,GovEmpInfo
# Register your models here.
admin.site.register(User)
admin.site.register(UserProPic)
admin.site.register(PatientInfo)
admin.site.register(DoctorInfo)
admin.site.register(PharInfo)
admin.site.register(OrgInfo)
admin.site.register(GovEmpInfo)

