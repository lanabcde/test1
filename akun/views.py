from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from .forms import FormRegistSiswa, FormRegistGuru, UserFormSiswa,GuruForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User,Siswa,Guru
from materi.models import QuizSubmission
from materi import models as MMODEL
from materi import forms as MFORM
from .filters import SiswaFilter
from materi.forms import QuizSubmissionFilterForm,KuisForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.loader import render_to_string
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
 

def login_guru(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password )
            if user is not None and user.is_guru :
                login(request,user)
                return redirect('home_guru')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'guru/login_guru.html',
    context={'form':AuthenticationForm()})

def login_siswa(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_siswa:
                login(request,user)
                return redirect('home_siswa')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'siswa/login_siswa.html',
    context={'form':AuthenticationForm()})

@login_required(login_url='login_siswa')
def home_siswa(request):

    return render(request,'siswa/home_siswa.html')

@login_required(login_url='login_siswa')
def profile_siswa(request):

    return render(request,'siswa/profile_siswa.html')

@login_required(login_url='login_guru')
def home_guru(request):

    return render(request,'guru/home_guru.html')


class regist_siswa(CreateView):
    model = User
    form_class = FormRegistSiswa
    template_name = 'siswa/regist_siswa.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login_siswa')

class regist_guru(CreateView):
    model = User
    form_class = FormRegistGuru
    template_name = 'guru/regist_guru.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login_guru')

@login_required(login_url='login_guru')
def hapus_siswa(request,pk):
    Siswa.objects.filter(pk=pk).delete()
    return redirect('data_siswa')


class edit_siswa(UpdateView):
    model = User
    form_class = UserFormSiswa
    template_name = 'guru/edit_siswa.html'

    def form_valid(self, form):
         form.save()
         return redirect('data_siswa')
    


def login_siswa(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('home_siswa')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'siswa/login_siswa.html',
    context={'form':AuthenticationForm()})


def login_guru(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('home_guru')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'guru/login_guru.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='login_guru')
def data_siswa(request):
    siswa_instances = Siswa.objects.all()
    siswa_filter = SiswaFilter(request.GET, queryset=siswa_instances)

    # Periksa apakah data sesuai dengan filter
    for siswa in siswa_filter.qs:
        print(siswa)

    return render(request, 'guru/data_siswa.html', {'siswa_filter': siswa_filter})

def export_to_pdf(request):
    # Mendapatkan data dari model Django
    quiz_submissions = QuizSubmission.objects.all()

    # Membuat file PDF baru
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="quiz_submissions.pdf"'

    # Membuat objek PDF
    pdf = SimpleDocTemplate(response, pagesize=letter)
    
    # Menyiapkan data untuk tabel PDF
    table_data = [['User', 'Kuis', 'Nilai', 'Submitted At']]  # Judul kolom
    for submission in quiz_submissions:
        table_data.append([submission.user.username, submission.quiz.title, submission.score, submission.submitted_at])  # Data dari model

    # Membuat tabel PDF
    table = Table(table_data)

    # Mengatur gaya tabel
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)

    # Menambahkan tabel ke objek PDF
    pdf.build([table])

    return response

@login_required(login_url='login_guru')
def data_hasil_belajar(request):
    quiz_submission_filter_form = QuizSubmissionFilterForm(request.GET)
    queryset = QuizSubmission.objects.all().order_by('-submitted_at')  # Urutkan dari yang terbaru hingga yang terlama

       # Periksa apakah permintaan adalah permintaan GET pertama kali
    if request.method == 'GET' and not request.GET:
        # Jika permintaan GET pertama kali, tampilkan semua data tanpa filter
        quiz_submission_filter_form = QuizSubmissionFilterForm()
    else:
        # Jika bukan permintaan GET pertama kali, terapkan filter yang diberikan
        if quiz_submission_filter_form.is_valid():
            quiz_id = quiz_submission_filter_form.cleaned_data.get('quiz')
            kelas_siswa = quiz_submission_filter_form.cleaned_data.get('kelas_siswa')

            if quiz_id:
                queryset = queryset.filter(quiz=quiz_id)
            
            if kelas_siswa:
                queryset = queryset.filter(user__siswa__kelas=kelas_siswa)

    # Paginasi
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 10)  # Tentukan jumlah item per halaman
    try:
        hasil_belajar = paginator.page(page)
    except PageNotAnInteger:
        hasil_belajar = paginator.page(1)
    except EmptyPage:
        hasil_belajar = paginator.page(paginator.num_pages)

    if 'print' in request.GET:
        

        # Render template ke HTML
        html_template = render_to_string('guru/hasil_belajar_print.html', {'hasil_belajar': hasil_belajar})

        # Konversi HTML ke PDF
        pdf = pdfkit.from_string(html_template, False)

        # Buat respons HTTP dengan tipe konten PDF
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="hasil_belajar.pdf"'
        return response
    
    return render(request, 'guru/hasil_belajar.html', {'quiz_submission_filter_form': quiz_submission_filter_form, 'hasil_belajar': hasil_belajar})

@login_required(login_url='login_guru')
def data_kuis(request):
    kuis = MMODEL.Quiz.objects.all()
    return render(request,'guru/data_kuis.html',{'kuis':kuis})

class edit_kuis(UpdateView):
    model = MMODEL.Quiz
    form_class = MFORM.KuisForm
    template_name = 'guru/edit_kuis.html'

    def form_valid(self, form):
         form.save()
         return redirect('data_kuis')

def profile_siswa(request, username):   
  # profile user
    user_object2 = User.objects.get(username=username)
    user_profile2 = Siswa.objects.get(user=user_object2)

    # request user
    user_object = User.objects.get(username=request.user)
    user_profile = Siswa.objects.get(user=user_object)

    submissions = QuizSubmission.objects.filter(user=user_object2)

    context = {"user_profile": user_profile, "user_profile2": user_profile2, "submissions":submissions}
    return render(request, "profile.html", context)

def hapus_hasil_belajar(request, pk):
    hasil_belajar = get_object_or_404(QuizSubmission, pk=pk)
    hasil_belajar.delete()
    return redirect('data_hasil_belajar')

@login_required(login_url='login_guru')
def guru_profile(request, pk):
    user = User.objects.get(pk=pk)
    guru = Guru.objects.get(user=user)
    context = {'guru': guru}
    return render(request, 'guru/profile_guru.html', context)

@login_required(login_url='login_siswa')
def siswa_profile(request, pk):
    user = User.objects.get(pk=pk)
    siswa = Siswa.objects.get(user=user)
    context = {'siswa': siswa}
    return render(request, 'siswa/profile_siswa.html', context)

class edit_guru_profile(UpdateView):
    model = User
    form_class = GuruForm
    template_name = 'guru/edit_profile_guru.html'

    def form_valid(self, form):
         form.save()
         return redirect('guru_profile',pk=self.request.user.pk)


# Create your views here.
