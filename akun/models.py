from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_guru = models.BooleanField(default=False)
    is_siswa = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Siswa(models.Model):
    OPSI_KELAS = [
        ('X MIPA 1', 'X MIPA 1'),
        ('X MIPA 2', 'X MIPA 2'),
        ('X MIPA 3', 'X MIPA 3'),
    ]

    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    nis = models.CharField(max_length=20, unique = True)
    email = models.EmailField(unique=True)
    kelas = models.CharField(max_length=20,  choices=OPSI_KELAS)
    progres = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Guru(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    nip = models.CharField(max_length=20, unique = True)
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
    
    
    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"