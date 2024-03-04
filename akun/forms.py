from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.db import transaction
from .models import User,Guru,Siswa

class FormRegistSiswa(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    nis = forms.CharField(required=True)
    email = forms.EmailField(required=False)

    # Tentukan pilihan untuk kolom kelas
    OPSI_KELAS = [
        ('X MIPA 1', 'X MIPA 1'),
        ('X MIPA 2', 'X MIPA 2'),
        ('X MIPA 3', 'X MIPA 3'),
    ]

    kelas = forms.ChoiceField(choices=OPSI_KELAS, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_siswa = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        
        siswa = Siswa.objects.create(user=user)
        siswa.nis = self.cleaned_data.get('nis')
        siswa.email = self.cleaned_data.get('email')
        siswa.kelas = self.cleaned_data.get('kelas')  # Gunakan cleaned_data untuk mengakses data formulir
        siswa.save()
        
        return user

class FormRegistGuru(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    nip = forms.CharField(required=True)
    no_hp = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_guru = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        guru = Guru.objects.create(user=user)
        guru.nip=self.cleaned_data.get('nip')
        guru.no_hp=self.cleaned_data.get('no_hp')
        guru.save()
        return user

class UserFormSiswa(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class FormSiswa(forms.ModelForm):
    class Meta:
        model=Siswa
        fields=['user','nis','email','kelas']

class GuruForm(forms.ModelForm):
    class Meta:
        model = Guru
        fields = ['nip', 'email']

        

