from django.shortcuts import render,redirect ,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from AccountApp.models import User,UserProPic,PatientInfo,DoctorInfo,PharInfo,OrgInfo,GovEmpInfo
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from managment_app.models import Verify


# Create your views here.






@login_required
def verify_acount(request, username):
    verify = User.objects.get(username=username)
    expecting_user = request.user
    alrady_follow = Verify.objects.filter(follower=expecting_user)
    if not alrady_follow:
        followed = Verify(follower=expecting_user)
        followed.save()
        return HttpResponseRedirect(reverse('blog_app:blog_list'))

        
@login_required
def unverify_acount(request, username):
    verify = User.objects.get(username=username)
    expecting_user = request.user
    alrady_follow = Verify.objects.filter(follower=expecting_user)
    alrady_follow.delete()
    return HttpResponseRedirect(reverse('blog_app:blog_list'))