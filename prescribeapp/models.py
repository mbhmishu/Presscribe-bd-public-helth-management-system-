from django.db import models
from AccountApp.models import User, DoctorInfo,PatientInfo

# Create your models here.

class Prescription(models.Model):
    doctor=models.ForeignKey(User, related_name='prescribe_giver', on_delete=models.CASCADE)
    patient=models.ForeignKey(User, related_name='prescribe_receiver', on_delete=models.CASCADE)
    test=models.TextField( verbose_name='Advice medical test...', blank=True, null=True )
    disease=models.TextField( verbose_name='Patient disease...', blank=True, null=True )
    prescrb=models.TextField(verbose_name='Prescribe medicine...', blank=True, null=True )
    Advice = models.TextField(verbose_name='Consult...', blank=True, null=True)
    prescrb_img=models.ImageField(upload_to='prescribeImg', verbose_name='Image', blank=True, null=True)
    creat_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-creat_date',)

    def __str__(self):
        return self.disease


class Review(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_receiver')
    giver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_giver')
    review=models.TextField()
    review_date=models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-review_date',]
    
    def __str__(self):
        return self.review


class Likes(models.Model):
    Review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='like_Review')
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likers')

    def __str__(self):
        return self.user + 'likes' + self.Review


class Permission(models.Model):
    permission_giver = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='permission_giver')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
    date = models.DateTimeField(auto_now_add=True)



class MedicaleRocord(models.Model):
    hospital=models.ForeignKey(User, related_name='m_record_giver', on_delete=models.CASCADE)
    patient=models.ForeignKey(User, related_name='m_record_receiver', on_delete=models.CASCADE)
    title = models.CharField(max_length=264,verbose_name='Record title ', blank=True, null=True)
    record=models.TextField(verbose_name='Medical record......', blank=True, null=True )
    Advice = models.TextField(verbose_name='Advice', blank=True, null=True)
    record_img=models.ImageField(upload_to='medical_record', verbose_name='Record Image', blank=True, null=True)
    creat_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-creat_date',)

    def __str__(self):
        return self.record



class MedicalTestReport(models.Model):
    lab=models.ForeignKey(User, related_name='m_report_giver', on_delete=models.CASCADE)
    patient=models.ForeignKey(User, related_name='m_report_receiver', on_delete=models.CASCADE)
    title = models.CharField(max_length=264,verbose_name='Report title ', blank=True, null=True)
    doctor=models.CharField( max_length=24,verbose_name='Dr. username', blank=True, null=True )
    report=models.TextField(verbose_name='Medical report......', blank=True, null=True )
    Advice = models.TextField(verbose_name='Advice', blank=True, null=True)
    report_img=models.ImageField(upload_to='TestReportImg', verbose_name='Report Image', blank=True, null=True)
    creat_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-creat_date',)

    def __str__(self):
        return self.title



class Reting(models.Model):
    retgiver = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='rating_giver')
    retrecipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reting_recipient')
    ret = [
    ('1', 'Freshman'),
    ('2', 'Sophomore'),
    ('3', 'Junior'),
    ('4', 'Senior'),
    ('5', 'Graduate'),
]
    num_stars = models.IntegerField()

    def __str__(self):
        return self.user + 'likes' + self.Review
    
    