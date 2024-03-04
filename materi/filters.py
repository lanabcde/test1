import django_filters
from .models import QuizSubmission

class QuizSubmissionFilter(django_filters.FilterSet):
    class Meta:
        model = QuizSubmission
        fields = ['quiz', 'user__siswa__kelas']