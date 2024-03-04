from django.urls import path
from .import  views

urlpatterns=[
     path('regist_siswa/',views.regist_siswa.as_view(), name='regist_siswa'),
     path('regist_guru/',views.regist_guru.as_view(), name='regist_guru'),
     path('edit_kuis/<int:pk>/',views.edit_kuis.as_view(), name='edit_kuis'),
     path('edit_siswa/<int:pk>/',views.edit_siswa.as_view(), name='edit_siswa'),
     path('login_siswa/',views.login_siswa, name='login_siswa'),
     path('login_guru/',views.login_guru, name='login_guru'),
     path('guru_profile/<int:pk>/',views.guru_profile, name='guru_profile'),
     path('siswa_profile/<int:pk>/',views.siswa_profile, name='siswa_profile'),
     path('edit_profile/<int:pk>/', views.edit_guru_profile.as_view(), name='edit_guru_profile'),
     path('logout/',views.logout_view, name='logout'),
     path('home_siswa',views.home_siswa,name='home_siswa'),
     path('profile_siswa',views.profile_siswa,name='profile_siswa'),
     path('hapus_siswa/<int:pk>/',views.hapus_siswa,name='hapus_siswa'),
     path('hapus_hasil_belajar/<int:pk>/', views.hapus_hasil_belajar, name='hapus_hasil_belajar'),
     path('home_guru',views.home_guru,name='home_guru'),
     path('data_siswa', views.data_siswa, name='data_siswa'),
     path('data_kuis', views.data_kuis, name='data_kuis'),
     path('data_hasil_belajar', views.data_hasil_belajar, name='data_hasil_belajar'),
     path('export_to_pdf',views.export_to_pdf,name='export_to_pdf'),
    
]   

