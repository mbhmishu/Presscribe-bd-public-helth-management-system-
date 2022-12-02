from django.shortcuts import render,redirect ,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from AccountApp.forms import UserProPicForm,Patien_RegisForm, Doc_RegisForm,Phar_RegisForm,PharFirm_RegisForm,Lab_RegisForm,UserEditForm,Hospi_RegisForm,User_SignInForm,DoctorInfoEdForm, PatientInfoEdForm,PharInfoEdForm,ORG_InfoEdForm,GovEmpEdForm,Govt_RegisForm
from AccountApp.models import User,UserProPic,PatientInfo,DoctorInfo,PharInfo,OrgInfo,GovEmpInfo
from django.contrib.auth.forms import AuthenticationForm,  UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from blogapp.models import Follow

from prescribeapp.forms import ReviewForm
from prescribeapp.models import Likes,Review
from managment_app.models import Verify




# SineUp views ####################################

def regi_type(request):
    return render(request, 'Account/register_type.html', context={})


def patient_regi(request):
    registerd = False
    form = Patien_RegisForm()
    if request.method == 'POST':
        form = Patien_RegisForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            registerd = True
            user_profile = PatientInfo(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('Accountapp:sign_in'))  
    return render (request, 'Account/patient_regi.html', context={'form':form , 'registerd':registerd}) 


def doctor_regi(request):
    form = Doc_RegisForm()
    if request.method == "POST":
        form = Doc_RegisForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = DoctorInfo(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('Accountapp:sign_in'))      
    return render(request, 'Account/doctor_regi.html', context={'form': form})



def pharmacy_regi(request):
    form = Phar_RegisForm()
    if request.method == 'POST':
        form = Phar_RegisForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = PharInfo(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('Accountapp:sign_in'))  
    return render(request, 'Account/pharmacy_regi.html', context={'form': form})


def labrotory_regi(request):
    form = Lab_RegisForm()
    if request.method == 'POST':
        form = Lab_RegisForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = OrgInfo(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('Accountapp:sign_in'))  
    return render(request, 'Account/labrotory_regi.html', context={'form': form})


def hospital_regi(request):
    form = Hospi_RegisForm()
    if request.method == 'POST':
        form = Hospi_RegisForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = OrgInfo(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('Accountapp:sign_in')) 
    return render(request, 'Account/hospital_regi.html', context={'form': form})



def pharmaciuticalfurm_resi(request):
    form = PharFirm_RegisForm()
    if request.method == 'POST':
        form = PharFirm_RegisForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = OrgInfo(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('Accountapp:sign_in'))
    return render(request, 'Account/pharmaciuticalfurm_resi.html', context={'form': form})



def gov_regi(request):
    form = Govt_RegisForm()
    if request.method == 'POST':
        form = Govt_RegisForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = GovEmpInfo(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('Accountapp:sign_in'))
    
    return render(request, 'Account/admin_regi.html', context={'form': form})




#SignIn SignOut views ###################################  
def sign_in(request):
    form = User_SignInForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_doctor:
                login(request, user)
                return HttpResponseRedirect(reverse('Accountapp:doc_dashboard'))
            elif user is not None and user.is_patient:
                login(request, user)
                return HttpResponseRedirect(reverse('Accountapp:patient_dashboard'))
            elif user is not None and user.is_pharmacy:
                login(request, user)
                return HttpResponseRedirect(reverse('Accountapp:pharmacy_dashboard'))
            elif user is not None and user.is_Govt:
                login(request, user)
                return HttpResponseRedirect(reverse('Accountapp:gov_dashbord')) 
            elif user is not None and user.is_pharmacy:
                login(request, user)
                return HttpResponseRedirect(reverse('Accountapp:pharmacy_dashboard')) 
            elif user is not None and user.is_labratory or user.is_hospital or user.is_pharmacuticalfarm:
                login(request, user)
                return HttpResponseRedirect(reverse('Accountapp:ORG_dashboard')) 
            elif user is not None and user.is_Govt :
                login(request, user)
                return HttpResponseRedirect(reverse('Accountapp:gov_dashbord'))
            return HttpResponseRedirect(reverse('Accountapp:notfound'))
    return render(request,'Account/login.html', context={'form':form, 'title':'Login'})


@login_required
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('Accountapp:sign_in'))

  
def index(request):
    return render(request, 'Account/base.html')

def notfound(request):
    return render(request, 'notfound.html')

# Profile views ##############################
@login_required
def doc_profile(request, username):
    result_user = User.objects.get(username=username)
    alrady_follow = Follow.objects.filter(follower=request.user,following=result_user)
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
    return render(request, 'Profile/doctor_profile.html', context={'result_user':result_user, 'review_form':review_form,'alrady_follow':alrady_follow})       
    
    

@login_required
def ORG_details(request, username):
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
            return HttpResponseRedirect(reverse('Accountapp:ORG_details' , kwargs={'username':username}))
    return render(request, 'org_details.html', context={'result_user':result_user, 'review_form':review_form})  
    

 



#User dashboard views ##############################
@login_required
def patient_dashboard(request):
    return render(request, 'Profile/patient_dashboard.html', context={})

@login_required
def doc_dashboard(request):
    patients = PatientInfo.objects.all()[0:5]
    if request.method == "GET":
        Search = request.GET.get('Search', '')
        results = User.objects.filter(username__icontains=Search)[0:1]
    return render(request, 'Profile/doctor_dashboard.html', context={'results':results,'Search':Search, 'patients':patients})


def pharmacy_dashboard(request):
    return render(request, 'Profile/org_dashboard.html', context={})

def ORG_dashboard(request):
    if request.method == "GET":
        Search = request.GET.get('Search', '')
        results = User.objects.filter(username__icontains=Search)[0:1]
    return render(request, 'Profile/org_dashboard.html', context={'results':results,'Search':Search})


@login_required
def gov_dashbord(request):
    user_list=User.objects.order_by('username')
    doctor_list=DoctorInfo.objects.all()
    patient_List = PatientInfo.objects.all()
    phar_list = PharInfo.objects.all()
    hospital_list = OrgInfo.objects.filter(user__is_hospital=True)
    lab_list = OrgInfo.objects.filter(user__is_labratory=True)
    pharmacuticalfarm_list = OrgInfo.objects.filter(user__is_pharmacuticalfarm=True)

    verified_doctor=User.objects.filter(expecting_ac__expecting__is_doctor=True)
    verified_phar=User.objects.filter(expecting_ac__expecting__is_pharmacy=True)
    verified_hospital=User.objects.filter(expecting_ac__expecting__is_hospital=True)
    verified_lab=User.objects.filter(expecting_ac__expecting__is_labratory=True)
    verified_phfarm=User.objects.filter(expecting_ac__expecting__is_pharmacuticalfarm=True)
    
    
    unverified_doctor=User.objects.exclude(expecting_ac__expecting__is_doctor=True).filter(is_doctor=True)
    unverified_phar=User.objects.exclude(expecting_ac__expecting__is_pharmacy=True).filter(is_pharmacy=True)
    unverified_hospital=User.objects.exclude(expecting_ac__expecting__is_hospital=True).filter(is_hospital=True)
    unverified_lab=User.objects.exclude(expecting_ac__expecting__is_labratory=True).filter(is_labratory=True)
    unverified_phfarm=User.objects.exclude(expecting_ac__expecting__is_pharmacuticalfarm=True).filter(is_pharmacuticalfarm=True)

    return render(request, 'Profile/gov_dashbord.html', context={'unverified_doctor':unverified_doctor,'verified_doctor':verified_doctor,'user_list':user_list,'doctor_list':doctor_list,'patient_List':patient_List,'phar_list':phar_list,'hospital_list':hospital_list,'lab_list':lab_list,'pharmacuticalfarm_list':pharmacuticalfarm_list,'verified_phar':verified_phar,'unverified_phar':unverified_phar,'verified_hospital':verified_hospital,'unverified_hospital':unverified_hospital,'verified_lab':verified_lab, 'unverified_lab':unverified_lab,'verified_phfarm':verified_phfarm,'unverified_phfarm':unverified_phfarm})  


@login_required
def review(request):
    return render(request, 'reviews.html', context={})

class DoctorList(ListView):
    context_object_name = 'blogs'
    model = DoctorInfo
    template_name = 'BlogApp/blog_list.html'  


# Search List View
@login_required
def search_all(request):
    user_list = User.objects.order_by('username')
    if request.method == "GET":
        Search = request.GET.get('Search', '')
        results = User.objects.filter(username__icontains=Search)
    return render(request, 'search.html', context={'results': results, 'Search': Search,'user_list':user_list})


@login_required
def view_all_profile(request, username):
    result_user = User.objects.get(username=username)
    if result_user.is_patient:
        if result_user == request.user:
            return HttpResponseRedirect(reverse('Accountapp:patient_dashboard'))
        return HttpResponseRedirect(reverse('prescrib:patient_profile' , kwargs={'username':username}))  
    elif result_user.is_doctor:
        if result_user == request.user:
            return HttpResponseRedirect(reverse('Accountapp:doc_dashboard'))
        return HttpResponseRedirect(reverse('Accountapp:doc_profile' , kwargs={'username':username}))
    elif result_user.is_pharmacy or result_user.is_labratory or result_user.is_hospital or result_user.is_pharmacuticalfarm:
        if result_user == request.user:
            return HttpResponseRedirect(reverse('Accountapp:ORG_dashboard'))
        return HttpResponseRedirect(reverse('Accountapp:ORG_details' , kwargs={'username':username}))       
         
    return HttpResponseRedirect(reverse('Accountapp:notfound'))




  
    


# user_profile_settings #################
@login_required
def patient_edit_pro(request):
    current_user = PatientInfo.objects.get(user=request.user)
    form = PatientInfoEdForm(instance=current_user)
    if request.method == "POST":
        form = PatientInfoEdForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = PatientInfoEdForm(instance=current_user)
            return HttpResponseRedirect(reverse('Accountapp:patient_dashboard'))
    return render(request, 'Profile/patient_profile_settings.html', context={'form':form})


@login_required
def doc_edit_pro(request):
    current_user = DoctorInfo.objects.get(user=request.user)
    form = DoctorInfoEdForm(instance=current_user)
    if request.method == 'POST':
        form = DoctorInfoEdForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Accountapp:doc_dashboard'))
    return render(request, 'Profile/doctor_profile_settings.html', context={'form':form})


@login_required 
def pharmacy_edit_pro(request):
    current_user = PharInfo.objects.get(user=request.user)
    form = PharInfoEdForm(instance=current_user)
    if request.method == 'POST':
        form = PharInfoEdForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Accountapp:pharmacy_dashboard'))
    return render(request, 'Profile/patient_profile_settings.html', context={'form':form})

@login_required 
def ORG_edit_pro(request):
    current_user = OrgInfo.objects.get(user=request.user)
    form = ORG_InfoEdForm(instance=current_user)
    if request.method == 'POST':
        form = ORG_InfoEdForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Accountapp:ORG_dashboard'))
    return render(request, 'Profile/patient_profile_settings.html', context={'form':form})


def Govt_edit_pro(request):
    current_user = GovEmpInfo.objects.get(user=request.user)
    form = GovEmpEdForm(instance=current_user)
    if request.method == "POST":
        form = GovEmpEdForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = GovEmpEdForm(instance=current_user)
            return HttpResponseRedirect(reverse('Accountapp:gov_dashbord'))
    return render(request, 'Profile/patient_profile_settings.html', context={'form':form})



@login_required
def ChangePasss(request):
    ps_msg = False
    current_user = request.user
    Change_passowrd = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, request.POST,)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Accountapp:index'))       
    return render(request,'Account/change_pass.html', context={'Change_passowrd':Change_passowrd})


@login_required
def ChangeUser(request):
    u_msg = False
    current_user = request.user
    form = UserEditForm(instance=current_user)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserEditForm(instance=current_user)
            if current_user.is_doctor:
                return HttpResponseRedirect(reverse('Accountapp:doc_dashboard'))
            elif current_user.is_patient:
                return HttpResponseRedirect(reverse('Accountapp:patient_dashboard'))
            elif current_user.is_pharmacy:
                return HttpResponseRedirect(reverse('Accountapp:pharmacy_dashboard')) 
            elif current_user.is_labratory or current_user.is_hospital or current_user.is_pharmacuticalfarm:
                return HttpResponseRedirect(reverse('Accountapp:ORG_dashboard'))
            elif current_user.is_Govt:
                return HttpResponseRedirect(reverse('Accountapp:gov_dashbord'))
            return HttpResponseRedirect(reverse('Accountapp:notfound'))
    return render(request,'Account/change_user.html', context={'form':form})












# user_profile_pic_settings ##############################

@login_required
def AddProPic(request):
    current_user = request.user
    form = UserProPicForm()
    if request.method=='POST':
        form=UserProPicForm(request.POST, request.FILES)
        if form.is_valid():
            user_obj=form.save(commit=False)
            user_obj.user=request.user
            user_obj.save()
            
            if current_user.is_doctor:
                return HttpResponseRedirect(reverse('Accountapp:doc_dashboard'))
            elif current_user.is_patient:
                return HttpResponseRedirect(reverse('Accountapp:patient_dashboard'))
            elif current_user.is_pharmacy:
                return HttpResponseRedirect(reverse('Accountapp:pharmacy_dashboard')) 
            elif current_user.is_labratory or current_user.is_hospital or current_user.is_pharmacuticalfarm:
                return HttpResponseRedirect(reverse('Accountapp:ORG_dashboard'))
            elif current_user.is_Govt:
                return HttpResponseRedirect(reverse('Accountapp:gov_dashbord'))
            return HttpResponseRedirect(reverse('Accountapp:notfound'))
    return render(request,'Account/ProfilePicForm.html', context={'form':form})


def ProPicChange(request):
    current_user = request.user
    cp_msg = False
    form = UserProPicForm(instance=request.user.user_profile)
    if request.method == 'POST':
        form = UserProPicForm(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            cp_msg = True
            if current_user.is_doctor:
                return HttpResponseRedirect(reverse('Accountapp:doc_dashboard'))
            elif current_user.is_patient:
                return HttpResponseRedirect(reverse('Accountapp:patient_dashboard'))
            elif current_user.is_pharmacy:
                return HttpResponseRedirect(reverse('Accountapp:pharmacy_dashboard')) 
            elif current_user.is_labratory or current_user.is_hospital or current_user.is_pharmacuticalfarm:
                return HttpResponseRedirect(reverse('Accountapp:ORG_dashboard'))
            elif current_user.is_Govt:
                return HttpResponseRedirect(reverse('Accountapp:gov_dashbord'))
            return HttpResponseRedirect(reverse('Accountapp:notfound'))      
    return render(request,'Account/ProfilePicForm.html', context={'form':form})


