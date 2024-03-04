from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from akun.models import Siswa,User
from .models import Quiz, Category, Question, Choice, QuizSubmission, UserRank
from django.db.models import Q,Sum
from materi.models import QuizSubmission
from django.contrib import messages
from django.http import HttpResponse
from materi import models as QMODEL
from django.shortcuts import get_object_or_404
from akun.views import login_siswa


# Create your views here.

@login_required(login_url='login_siswa')
def semua_kuis(request):

    user_object = User.objects.get(username=request.user)
    user_profile = Siswa.objects.get(user=user_object)

    quizzes = Quiz.objects.order_by('-created_at')
    categories = Category.objects.all()

    context = {"user_profile": user_profile, "quizzes": quizzes, "categories": categories}
    return render(request, 'materi/semua_kuis.html', context)

@login_required(login_url='login_siswa')
def kuis_bab1(request):

    user_object = User.objects.get(username=request.user)
    user_profile = Siswa.objects.get(user=user_object)

    quizzes = Quiz.objects.order_by('-created_at')
    categories = Category.objects.all()

    context = {"user_profile": user_profile, "quizzes": quizzes, "categories": categories}
    return render(request, 'materi/kuis_bab1.html', context)


@login_required(login_url='login_siswa')
def kuis_view(request, quiz_id):
    user_object = request.user
    user_profile = Siswa.objects.get(user=user_object)
    quiz = get_object_or_404(Quiz, id=quiz_id)
    print("***** kkm *****", quiz.kkm)
    total_questions = quiz.question_set.all().count()

    if request.method == "POST":
        # Get the score
        score = int(request.POST.get('score', 0))
        if score < quiz.kkm :
             print(f"KKM for quiz {quiz.title}: {quiz.kkm}")
            
        else:   
                if quiz_id == 1 :
                    if user_profile.progres > 0:
                        pass
                    else:
                        user_profile.progres = 1
                        user_profile.save() 
                if quiz_id == 2 :
                    if user_profile.progres > 1:
                        pass
                    else:
                        user_profile.progres = 2
                        user_profile.save() 
                if quiz_id == 3 :
                    if user_profile.progres > 2:
                        pass
                    else:
                        user_profile.progres = 3
                        user_profile.save()
                if quiz_id == 4 :
                    if user_profile.progres > 3:
                        pass
                    else:
                        user_profile.progres = 4
                        user_profile.save() 
                if quiz_id == 5:
                    if user_profile.progres > 4:
                        pass
                    else:
                        user_profile.progres = 5
                        user_profile.save() 
                if quiz_id == 6 :
                    if user_profile.progres > 5:
                        pass
                    else:
                        user_profile.progres = 6
                        user_profile.save() 
                if quiz_id == 7 :
                    if user_profile.progres > 6:
                        pass
                    else:
                        user_profile.progres = 7
                        user_profile.save() 
        
         
        print("progxxxxxxxxxxxxres", user_profile.progres)
      
      
       # user_profile.progres += 1
       # user_profile.save()
        # user_profile.save()
        # print("user", user_profile)
        # print("user xxxx", type(user_profile))
        
        # Check if the user has already submitted the quiz
        kkm = quiz.kkm  # Gantilah ini dengan nama field yang sesuai pada model Quiz
        print(f"KKM for quiz {quiz.title}: {kkm}")

    
         # Reset waktu kuis dengan menghapus item quizTimer dari sesi
        if 'quizTimer' in request.session:
            del request.session['quizTimer']
    
        # Save the new quiz submission
        submission = QuizSubmission(user=request.user, quiz=quiz, score=score)
        submission.save()
        return redirect('hasil_kuis', quiz_id=quiz_id)

    context = {"user_profile": user_profile, "quiz": quiz}
    return render(request, 'materi/kuis.html', context)

@login_required(login_url='login_siswa')
def soal_evaluasi(request, quiz_id):
    user_object = request.user
    user_profile = Siswa.objects.get(user=user_object)
    quiz = get_object_or_404(Quiz, id=quiz_id)
    print("***** kkm *****", quiz.kkm)
    total_questions = quiz.question_set.all().count()

    if request.method == "POST":
        # Get the score
        score = int(request.POST.get('score', 0))
        if score < quiz.kkm :
             print(f"KKM for quiz {quiz.title}: {quiz.kkm}")
        else: 
               
                if quiz_id == 1 :
                    if user_profile.progres > 0:
                        pass
                    else:
                        user_profile.progres = 1
                        user_profile.save() 
                if quiz_id == 2 :
                    if user_profile.progres > 1:
                        pass
                    else:
                        user_profile.progres = 2
                        user_profile.save() 
                if quiz_id == 3 :
                    if user_profile.progres > 2:
                        pass
                    else:
                        user_profile.progres = 3
                        user_profile.save()
                if quiz_id == 4 :
                    if user_profile.progres > 3:
                        pass
                    else:
                        user_profile.progres = 4
                        user_profile.save() 
                if quiz_id == 5:
                    if user_profile.progres > 4:
                        pass
                    else:
                        user_profile.progres = 5
                        user_profile.save() 
                if quiz_id == 6 :
                    if user_profile.progres > 5:
                        pass
                    else:
                        user_profile.progres = 6
                        user_profile.save() 
                if quiz_id == 7 :
                    if user_profile.progres > 6:
                        pass
                    else:
                        user_profile.progres = 7
                        user_profile.save() 
        
         
        print("progxxxxxxxxxxxxres", user_profile.progres)
      
      
       # user_profile.progres += 1
       # user_profile.save()
        # user_profile.save()
        # print("user", user_profile)
        # print("user xxxx", type(user_profile))
        
        # Check if the user has already submitted the quiz
        kkm = quiz.kkm  # Gantilah ini dengan nama field yang sesuai pada model Quiz
        print(f"KKM for quiz {quiz.title}: {kkm}")
    
        # Save the new quiz submission
        submission = QuizSubmission(user=request.user, quiz=quiz, score=score)
        submission.save()
        return redirect('hasil_kuis', quiz_id=quiz_id)

    context = {"user_profile": user_profile, "quiz": quiz}
    return render(request, 'materi/soal_evaluasi.html', context)

def hasil_kuis(request, quiz_id):
    user_object = request.user
    user_profile = Siswa.objects.get(user=user_object)
    
    # Ambil objek QuizSubmission yang sesuai
    quiz_submission = QuizSubmission.objects.filter(user=user_object, quiz_id=quiz_id).last()

    if not quiz_submission:
        # Redirect ke halaman materi jika pengguna belum menyelesaikan kuis
        return redirect('nama_halaman_materi')

    # Ambil objek kuis
    quiz = get_object_or_404(Quiz, id=quiz_id)

    # Hitung jumlah soal yang dijawab benar
    total_correct_answers = quiz_submission.score // 20  # Setiap soal bernilai 20 poin
    total_questions = quiz.question_set.all().count()

    # Dapatkan nilai KKM dari objek kuis
    kkm = quiz.kkm

    context = {
        'total_correct_answers': total_correct_answers,
        'total_questions': total_questions,
        'score': quiz_submission.score,
        'quiz_title': quiz.title,
        'quiz_id': quiz_id,
        'kkm': kkm  # Masukkan nilai KKM ke dalam konteks
    }

    return render(request, 'materi/hasil_kuis.html', context)


@login_required(login_url='login_siswa')
def home_siswa(request):


    return render(request, "siswa/home_siswa.html")

@login_required(login_url='login_siswa')
def beranda_1(request):
  

    return render(request,'materi/p1_beranda.html')

@login_required(login_url='login_siswa')
def program(request):
  

    return render(request,'materi/p2_program.html')

@login_required(login_url='login_siswa')
def bahasa_pemrograman(request):
  

    return render(request,'materi/p3_bahasa_pemrograman.html')

@login_required(login_url='login_siswa')
def interpreter_compiler(request):
  

    return render(request,'materi/p4_interpreter_compiler.html')

@login_required(login_url='login')
def bahasa_python(request):
  

    return render(request,'materi/p5_bahasa_python.html')

@login_required(login_url='login_siswa')
def program_sederhana(request):
  

    return render(request,'materi/p7_program_sederhana.html')


@login_required(login_url='login_siswa')
def beranda2(request):
  

    return render(request,'materi/beranda2.html')

@login_required(login_url='login_siswa')
def tipe_data(request):
  

    return render(request,'materi/p8_tipe_data.html')

@login_required(login_url='login_siswa')
def variabel(request):
  

    return render(request,'materi/p9_variabel.html')

@login_required(login_url='login_siswa')
def operator(request):
  

    return render(request,'materi/p10_operator.html')


@login_required(login_url='login_siswa')
def kuis_bab2(request):
  

    return render(request,'materi/kuis_bab2.html')


@login_required(login_url='login_siswa')
def beranda3(request):
  

    return render(request,'materi/p11_beranda3.html')


@login_required(login_url='login_siswa')
def percabangan(request):
  

    return render(request,'materi/p12_percabangan.html')


@login_required(login_url='login_siswa')
def percabangan_if(request):
  

    return render(request,'materi/p_percabangan_if.html')


@login_required(login_url='login_siswa')
def percabangan_if_else(request):
  

    return render(request,'materi/p13_percabangan_if_else.html')

@login_required(login_url='login_siswa')
def percabangan_elif(request):
  

    return render(request,'materi/p14_percabangan_elif.html')

@login_required(login_url='login_siswa')
def percabangan_bersarang(request):

    return render(request, 'materi/percabangan_bersarang.html')

@login_required(login_url='login_siswa')
def kuis_bab3(request):
  

    return render(request,'materi/kuis_bab3.html')

@login_required(login_url='login_siswa')
def beranda4(request):
  

    return render(request,'materi/p15_beranda4.html')

@login_required(login_url='login_siswa')
def perulangan(request):
  

    return render(request,'materi/p16_perulangan.html')

@login_required(login_url='login_siswa')
def perulangan_while(request):
  

    return render(request,'materi/p17_perulangan_while.html')

@login_required(login_url='login_siswa')
def perulangan_for(request):
  

    return render(request,'materi/p18_perulangan_for.html')

@login_required(login_url='login_siswa')
def kuis_bab4(request):
  

    return render(request,'materi/kuis_bab4.html')

@login_required(login_url='login_siswa')
def beranda5(request):
  

    return render(request,'materi/p19_beranda5.html')

@login_required(login_url='login_siswa')
def fungsi(request):
  

    return render(request,'materi/p20_fungsi.html')

@login_required(login_url='login_siswa')
def membuat_fungsi(request):
  

    return render(request,'materi/p21_membuat_fungsi.html')

@login_required(login_url='login_siswa')
def cara_kerja_fungsi(request):
  

    return render(request,'materi/p22_cara_kerja_fungsi.html')

@login_required(login_url='login_siswa')
def parameterisasi_fungsi(request):
  

    return render(request,'materi/p23_parameterisasi_fungsi.html')

@login_required(login_url='login_siswa')
def variabel_lokal_global(request):


    return render(request,'materi/variabel_lokal_global.html')

@login_required(login_url='login_siswa')
def parameter_formal_aktual(request):

    return render(request,'materi/parameter_formal_aktual.html')

@login_required(login_url='login_siswa')
def parameter_wajib_opsional(request):

    return render(request,'materi/parameter_wajib_opsional.html')


@login_required(login_url='login_siswa')
def sintak_dasar(request):

    return render(request,'materi/sintak_dasar.html')


@login_required(login_url='login_siswa')
def komentar(request):

    return render(request, 'materi/komentar.html')

@login_required(login_url='login_siswa')
def operator_perbandingan(request):

    return render(request, 'materi/operator_perbandingan.html')


@login_required(login_url='login_siswa')
def operator_penugasan(request):

    return render(request, 'materi/operator_penugasan.html')


@login_required(login_url='login_siswa')
def operator_logika(request):

    return render(request, 'materi/operator_logika.html')


@login_required(login_url='login_siswa')
def input(request):

    return render(request, 'materi/input.html')

def output(request):

    return render(request, 'materi/output.html')


@login_required(login_url='login_siswa')
def beranda3(request):

    return render(request, 'materi/beranda3.html')


@login_required(login_url='login_siswa')
def kuis_bab5(request):

    return render(request, 'materi/kuis_bab5.html')


@login_required(login_url='login_siswa')
def beranda6(request):

    return render(request, 'materi/beranda6.html')


@login_required(login_url='login_siswa')
def kuis_bab6(request):

    return render(request, 'materi/kuis_bab6.html')


@login_required(login_url='login_siswa')
def beranda7(request):

    return render(request, 'materi/beranda7.html')

@login_required(login_url='login_siswa')
def kuis_bab7(request):

    return render(request, 'materi/kuis_bab7.html')

@login_required(login_url='login_siswa')
def evaluasi(request):

    return render(request,'materi/evaluasi.html')