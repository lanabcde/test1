from django import forms
from .models import Quiz
from akun.models import Siswa

class KuisForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'kkm'] 

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'kkm': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class QuizSubmissionFilterForm(forms.Form):
    quiz = forms.ModelChoiceField(queryset=Quiz.objects.all(), required=False, label='Kuis')
    kelas_siswa = forms.ChoiceField(choices=[('', '---')] + Siswa.OPSI_KELAS, required=False, label='Kelas Siswa apa')