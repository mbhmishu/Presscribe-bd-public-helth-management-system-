from django.db import models
from AccountApp.models import User,GovEmpInfo

# Create your models here.


class Verify(models.Model):
    toverify = models.ForeignKey(GovEmpInfo, on_delete=models.CASCADE ,related_name='to_verify')
    expecting = models.OneToOneField(User, on_delete=models.CASCADE, related_name='expecting_ac')
    date = models.DateTimeField(auto_now_add=True)
