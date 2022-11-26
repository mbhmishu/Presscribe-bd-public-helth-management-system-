from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_Govt = models.BooleanField('Is Government', default=False)
    is_doctor = models.BooleanField('Is doctor', default=False)
    is_patient = models.BooleanField('Is patient', default=False)
    is_pharmacy = models.BooleanField('Is pharmacy', default=False)
    is_pharmacuticalfarm = models.BooleanField('Is pharmacutical farm',default=False)
    is_labratory = models.BooleanField('Is labratory', default=False)
    is_hospital = models.BooleanField('Is hospital', default=False)






    
    
    



class Verify(models.Model):
    toverify = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='to_verify')
    expecting = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expecting_ac')
    date = models.DateTimeField(auto_now_add=True)




BloodGroup=(

    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
    ('O+','O+'),
    ('O-','O-'),
)



gander = (
    ('Maile','Maile'),
    ('Femail','Femail'),

)

Ph_Reg_Type = (
    ('B.Pharm(A)','B.Pharm(A)'),
    ('Diploma in pharmacy(B)', 'Diploma in pharmacy(B)'),
    ('Pharmacy Technician(C)','Pharmacy Technician(C)'),
)

Doc_Reg_Type = (
    ('Medical','Medical'),
    ('Dental', 'Dental'),
    ('Medical assistant','Medical assistant'),
    ('Foreign Doctor', 'Foreign Doctor'),
)



############### user info models_module

class UserProPic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    proPic = models.ImageField(upload_to='user_profile_pic', blank=True, null=True)



class DoctorInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_info')
    BmdcRegiNo =models.IntegerField(unique=True, blank=True, null=True)
    reg_type =models.CharField(max_length=25, choices=Doc_Reg_Type, blank=True, null=True)
    date_of_birth= models.DateField(blank=True, null=True)
    Gender = models.CharField(choices=gander,max_length=24, blank=True, null=True)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    services= models.CharField(max_length=264, blank=True, null=True)
    specialization= models.CharField(max_length=264, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    Degree = models.CharField(max_length=264, blank=True, null=True)
    work_location = models.CharField(max_length=264, blank=True, null=True)

    def __str__(self):
        return self.user.username
    

class PatientInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_info')
    date_of_birth= models.DateField(blank=True, null=True)
    blood_group =models.CharField( max_length=5, choices=BloodGroup)
    Gender = models.CharField(choices=gander, max_length=24)
    weight = models.CharField( max_length=24,blank=True, null=True)
    height = models.CharField( max_length=24,blank=True, null=True)
    contuct_no = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username




class PharInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pharmeci_info')
    RegiNo =models.CharField(unique=True, max_length=30, null=True, blank=True)
    org_type =models.CharField(max_length=25, choices=Ph_Reg_Type,null=True, blank=True)
    division =models.CharField( max_length=24 , blank=True, null=True)
    district = models.CharField(max_length=24, blank=True, null=True)
    upazilla = models.CharField(max_length=24, blank=True, null=True)
    last_updated_regi = models.DateField(null=True, blank=True)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    services= models.CharField(max_length=264, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    fb = models.URLField(blank=True, null=True)
    tw = models.URLField(blank=True, null=True)
    instra = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=264, blank=True, null=True)

    def __str__(self):
        return self.user.username




class OrgInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='org_info')
    RegiNo =models.CharField(unique=True, max_length=30, null=True, blank=True)
    org_type = models.CharField( max_length=264, blank=True, null=True)
    division =models.CharField( max_length=24 , blank=True, null=True)
    district = models.CharField(max_length=24, blank=True, null=True)
    upazilla = models.CharField(max_length=24, blank=True, null=True)
    last_updated_regi = models.DateField(null=True, blank=True)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    services= models.CharField(max_length=264, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    fb = models.URLField(blank=True, null=True)
    tw = models.URLField(blank=True, null=True)
    instra = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=264, blank=True, null=True)


class GovEmpInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='govt_emp_info')
    emp_id =models.IntegerField(unique=True, blank=True, null=True)
    emp_type =models.CharField(max_length=25, choices=Doc_Reg_Type, blank=True, null=True)
    date_of_birth= models.DateField(blank=True, null=True)
    Gender = models.CharField(choices=gander,max_length=24, blank=True, null=True)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.user.username