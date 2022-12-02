from django.shortcuts import render,redirect ,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from AccountApp.models import User,UserProPic,PatientInfo,DoctorInfo,PharInfo,OrgInfo,GovEmpInfo
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from managment_app.models import Verify


# Create your views here.

def verify_author(request):
    verified_doctor=User.objects.filter(expecting_ac__expecting__is_doctor=True)
    verified_phar=User.objects.filter(expecting_ac__expecting__is_pharmacy=True)
    verified_hospital=User.objects.filter(expecting_ac__expecting__is_hospital=True)
    verified_lab=User.objects.filter(expecting_ac__expecting__is_labratory=True)
    verified_phfarm=User.objects.filter(expecting_ac__expecting__is_pharmacuticalfarm=True)
    return render(request, 'management/user_list.html', context={'verified_doctor':verified_doctor,'verified_phar':verified_phar,'verified_hospital':verified_hospital,'verified_lab':verified_lab,'verified_phfarm':verified_phfarm,})  





@login_required
def verify_acount(request, username):
    expecting_user= User.objects.get(username=username)
    verify_user=request.user
    verify = Verify(toverify=verify_user.govt_emp_info,expecting=expecting_user)
    verify.save()
    return HttpResponseRedirect(reverse('Accountapp:gov_dashbord'))

        
@login_required
def unverify_acount(request, username):
    verify = User.objects.get(username=username)
    expecting_user = request.user
    alrady_follow = Verify.objects.filter(follower=expecting_user)
    alrady_follow.delete()
    return HttpResponseRedirect(reverse('blog_app:blog_list'))