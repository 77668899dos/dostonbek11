from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth.models import User
from app.models import CustomUser, Session_Time,Course,Student
from django.contrib import messages
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate,login,logout
def REGISTER(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password= request.POST.get('password')
        user_type= request.POST.get('user_type')
        profile_pic = request.FILES.get('profile_pic')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Bu email allaqachon mavjud')
            return redirect('register')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Bu Nom allaqachon mavjud')
            return redirect('register')

        user = CustomUser(
            email = email,
            username=username,
            user_type = user_type,
            profile_pic = profile_pic
        )
        user.set_password(password)
        user.save()
        return redirect('login')
    return render(request,'registration/register.html')

def LOGIN(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = EmailBackend.authenticate(request,
                                         username=email,
                                         password=password)
        if user != None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('direktor')
            elif user_type == '2':
                return HttpResponse('Ustoz sahifaga xush kelibsiz')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Login yoki parol xato')
            return redirect('login')

    return render(request,'registration/login.html')

def PROFILE(request):
    return render(request, 'Main/profile.html')

def LOGOUT(request):
    logout(request)
    return redirect('login')

def EDITPROFILE(request):
    return render(request, 'Main/edit-profile.html')
def UPDATEPROFILE(request):
    if request.method == 'POST':
        u_id = request.POST.get('id')
        u_email = request.POST.get('email')
        u_username = request.POST.get('username')
        u_firstName = request.POST.get('first_name')
        u_lastName = request.POST.get('last_name')

        try:
            user = User.objects.get(id = request.user.id)
            user.email = u_email
            user.username = u_username
            user.first_name = u_firstName
            user.last_name = u_lastName
            user.save()
            messages.success(request, 'Malumotlar yangilandi')
            return redirect('profile')

        except:
            messages.error(request, 'Nimadir xato')
            return redirect('editProfile')
    return redirect('profile')
# Admin

def DIREKTOR(request):
    return  render(request, 'admin/index.html')
def ADDSTUDENT(request):
    course = Course.objects.all()
    session = Session_Time.objects.all()

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gen = request.POST.get('gen')
        session_time = request.POST.get('session_time')
        course_id = request.POST.get('course_id')
        profile_pic = request.FILES.get('rasm')
        address = request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Bu Email allaqachon mavjud')
            return redirect('add_student')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Bu Nom allaqachon mavjud')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id = course_id)
            session_vaqt = Session_Time.objects.get(id = session_time)
            student = Student(
                admin = user,
                address= address,
                course_id = course,
                session_id = session_vaqt,
                gender = gen
            )
            student.save()
            messages.success(request,'Student muvaffaqqiyatli qo`shildi')
            return redirect('add_student')


    context = {
        'course': course,
        'session': session
    }
    return render(request, 'admin/add_student.html',context=context)

def VIEWSTUDENT(request):
    student = Student.objects.all()
    context = {
        'student': student
    }
    return render(request, 'admin/view_student.html',context=context)
def EDITSTUDENT(request,id):
    student = Student.objects.get(id = id)
    course = Course.objects.all()
    sessiya = Session_Time.object.all()
    context = {
        'student': student,
        'course':course,
        'sessiya':sessiya
    }
    return render(request, 'admin/edit_student.html',context=context)

def UPDATESTUDENT(request):
            if request.method == 'POST':
                student_id = request.POST.get('id')
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                username = request.POST.get('username')
                gen = request.POST.get('gen')
                profile_pic = request.FILES.get('profile_pic')
                email = request.POST.get('email')
                password = request.POST.get('password')
                session_time = request.POST.get('session_time')
                course_id = request.POST.get('course_id')
                address = request.POST.get('address')
                user = CustomUser.objects.get(id = student_id)
                user.first_name = first_name
                user.last_name = last_name
                user.username = username
                user.email = email
                if password != None and password != '' :
                   user.set_password(password)
                if profile_pic != None and profile_pic != '' :
                    user.profile_pic = profile_pic
                user.save()
                student = Student.objects.get(admin = student_id)
                student.address = address
                student.gender = gen
                course = Course.objects.get(id = student_id)
                student.course_id = course
                session = Session_Time.objects.get(id = session_time)
                student.session_id = session
                student.save()
                messages.success(request, 'Malumot muvaffaqqiyatli yangilandi')
                return redirect('view_student')
            return redirect('view_student')

def DELETESTUDENT(request,id):
    student = CustomUser.objects.get(id = id)
    student.delete()
    messages.success(request,'Malumot muvaffaqqiyatli o`chirildi')
    return redirect('view_student')

# kurs
def ADDCOURSE(request):
    if request.method == 'POST':
        name = request.POST.get('course_name')
        course = Course(
            name = name
        )
        course.save()
        messages.success(request, 'yangi kurs qo`shildi')
    return render(request,'admin/add_course.html')

def VIEWCOURSE(request):
    course = Course.objects.all()
    context = {
        'course': course
    }
    return render(request, 'admin/view_course.html', context=context)

def EDITCOURSE(request,id):
    course = Course.objects.get(id = id)
    context = {
        'course': course
    }
    return render(request, 'admin/edit_course.html',context=context)
def UPDATECOURSE(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course_id = request.POST.get('id')

        course = Course.objects.get(id = course_id)
        course.name = course_name
        course.save()
        messages.success(request, 'kurs yangilandi')
        return redirect('view_course')

def DELETECOURSE(request,id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request, 'Kurs muvaffaqiyatli o`childi')
    return redirect('view_course')

# session

def ADDSESSION(request):
    if request.method == 'POST':
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')

        session = Session_Time(
            sesstion_start = session_start,
            sesstion_end = session_end,
         )
        session.save()
        messages.success(request,'yangi vaqt qo`shildi')
        return render(request, 'admin/add_session.html')
def VIEWSESSION(request):
    session = Session_Time.objects.all()
    context = {
         'session':session
    }
    return render(request, 'admin/view_session.html', context=context)

def EDITSESSION(request,id):
    session = Session_Time.objects.get(id = id)
    context = {
        'session': session
    }
    return render(request,'admin/edit_session.html',context=context)

def UPDATESESSION(request):
    if request.method == 'POST':
        session_start = request.POST.get('session_start')
        session_and = request.POST.get('session_end')
        id = request.POST.get('id')

        session = Session_Time.objects.get(id = id)
        session.session_start = session_start
        session.session_and = session_end
        session.save()
        messages.success(request, 'Sessiya yangilandi')
        return redirect('view_session')


def DELETESESSION(request,id):
    session = Session_Time.objects.get(id = id)
    session.delete()
    messages.success(request, 'Kurs muvaffaqiyatli o`childi')
    return redirect('view_session')