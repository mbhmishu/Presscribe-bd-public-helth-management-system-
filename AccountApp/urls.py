from django.urls import path
from AccountApp import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'Accountapp'

urlpatterns = [
    path('signin/', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('', views.index, name='index'),
    path('regi_type/', views.regi_type, name='regi_type'),
    path('patient_regi/', views.patient_regi, name='patient_regi'),
    path('doctor_regi/', views.doctor_regi, name='doctor_regi'),
    path('pharmacy_regi/', views.pharmacy_regi, name='pharmacy_regi'),
    path('labrotory_regi/', views.labrotory_regi, name='labrotory_regi'),
    path('hospital_regi/', views.hospital_regi, name='hospital_regi'),
    path('gov_regi/', views.gov_regi, name='gov_regi'),
    path('pharmaciuticalfurm_resi/', views.pharmaciuticalfurm_resi, name='pharmaciuticalfurm_resi'),
    path('doc_dashboard/', views.doc_dashboard, name='doc_dashboard'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('gov_dashbord/', views.gov_dashbord, name='gov_dashbord'),
    path('pharmacy_dashboard/', views.pharmacy_dashboard, name='pharmacy_dashboard'),
    path('ORG_dashboard/', views.ORG_dashboard, name='ORG_dashboard'),
    path('patient_edit_pro/', views.patient_edit_pro, name='patient_edit_pro'),
    path('doc_edit_pro/', views.doc_edit_pro, name='doc_edit_pro'),
    path('pharmacy_edit_pro/', views.pharmacy_edit_pro, name='pharmacy_edit_pro'),
    path('ORG_edit_pro/', views.ORG_edit_pro, name='ORG_edit_pro'),
    path('Govt_edit_pro/', views.Govt_edit_pro, name='Govt_edit_pro'),
    path('doc_profile/<username>/', views.doc_profile, name='doc_profile'),
    path('review/', views.review, name='review'),
    path('search_all/', views.search_all, name='search'),
    path('ChangePasss/', views.ChangePasss, name='ChangePasss'),
    path('ChangeUser/', views.ChangeUser, name='ChangeUser'),
    path('AddProPic/', views.AddProPic, name='AddProPic'),
    path('ProPicChange/', views.ProPicChange, name='ProPicChange'),
    path('view_all_profile/<username>/', views.view_all_profile, name='view_all_profile'),
    path('patient_dtl_viw/<username>/', views.patient_dtl_viw, name='patient_dtl_viw'),
    path('ORG_details/<username>/', views.ORG_details, name='ORG_details'),
     path('notfound',views.notfound, name='notfound'),
    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
