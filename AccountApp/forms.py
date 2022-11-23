from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from AccountApp.models import User,UserProPic,PatientInfo,DoctorInfo,PharInfo,OrgInfo,GovEmpInfo


# Rgistratuon forms ######################
class Patien_RegisForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'usernam'}),label='')
    first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),label='')
    last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}),label='')
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),label='')
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}),label='')
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'@Email'}),label='')
    is_patient = forms.BooleanField(required=True , label='Im a patient')

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'password1', 'password2', 'email','is_patient')


class Doc_RegisForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'usernam'}),label='')
    first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),label='')
    last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}),label='')
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),label='')
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}),label='')
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'@Email'}),label='')
    is_doctor = forms.BooleanField(required=True , label='Im a patient')
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'password1', 'password2', 'email','is_doctor')


class Lab_RegisForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'usernam'}),label='')
    first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),label='')
    last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}),label='')
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),label='')
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}),label='')
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'@Email'}),label='')
    is_labratory = forms.BooleanField(required=True , label='Im a patient')

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'password1', 'password2', 'email','is_labratory')


class Phar_RegisForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'usernam'}),label='')
    first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),label='')
    last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}),label='')
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),label='')
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}),label='')
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'@Email'}),label='')
    is_pharmacy = forms.BooleanField(required=True , label='Im a patient')

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'password1', 'password2', 'email','is_pharmacy')


class Hospi_RegisForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'usernam'}),label='')
    first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),label='')
    last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}),label='')
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),label='')
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}),label='')
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'@Email'}),label='')
    is_hospital = forms.BooleanField(required=True , label='Im a patient')
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'password1', 'password2', 'email','is_hospital')


class PharFirm_RegisForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'usernam'}),label='')
    first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),label='')
    last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}),label='')
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),label='')
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}),label='')
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'@Email'}),label='')
    is_pharmacuticalfarm = forms.BooleanField(required=True , label='Im a patient')

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'password1', 'password2', 'email','is_pharmacuticalfarm')  


class Govt_RegisForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'usernam'}),label='')
    first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),label='')
    last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}),label='')
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),label='')
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}),label='')
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'@Email'}),label='')
    is_Govt = forms.BooleanField(required=True , label='Im a patient')

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'password1', 'password2', 'email','is_Govt')


#Login Form #################################
class User_SignInForm(AuthenticationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'usernam'}),label='username')
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),label='Password')
    
    class Meta:
        model = User
        fields = ('username', 'password')


# Profile Ssting Form ##########################
class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','password')


class DoctorInfoEdForm(forms.ModelForm):
    date_of_birth = forms.DateField(label='Date of birth',widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model = DoctorInfo
        exclude = ('user',)


class PatientInfoEdForm(forms.ModelForm):
    date_of_birth = forms.DateField(label='Date of birth',widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model = PatientInfo
        exclude = ('user',)


class PharInfoEdForm(forms.ModelForm):
    D_O_B = forms.DateField(label='Date of birth',widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model = PharInfo
        exclude = ('user',)

class ORG_InfoEdForm(forms.ModelForm):
    date_of_birth = forms.DateField(label='Date of birth',widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model = PatientInfo
        exclude = ('user',)

class GovEmpEdForm(forms.ModelForm):
    date_of_birth = forms.DateField(label='Date of birth',widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model = GovEmpInfo
        exclude = ('user',)


class UserProPicForm(forms.ModelForm):
    class Meta:
        model = UserProPic
        fields = ['proPic']

      


