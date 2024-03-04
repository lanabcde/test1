import django_filters
from .models import *
from materi.models import *

class SiswaFilter(django_filters.FilterSet):
    class Meta:
        model = Siswa
        fields = ['kelas']