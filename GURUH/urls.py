from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views, user_login

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('api.urls')),

    path('base/', views.BASE, name='base'),

    path('', views.HOME, name='home'),

    path('about/', views.ABOUT, name='about'),


    path('register/', user_login.REGISTER, name='register'),
    path('profile/', user_login.PROFILE, name='profile'),
    path('login/', user_login.LOGIN, name='login'),
    path('logout/', user_login.LOGOUT, name='logout'),
    path('edit-profile/', user_login.EDITPROFILE, name='editProfile'),
    path('update-profile/', user_login.UPDATEPROFILE, name='updateProfile'),
    path('direktor/', user_login.DIREKTOR, name='direktor'),
    path('direktor/add_student', user_login.ADDSTUDENT, name='add_student'),
    path('direktor/view_student', user_login.VIEWSTUDENT, name='view_student'),
    path('direktor/edit_student/<str:id>', user_login.EDITSTUDENT, name='edit_student'),
    path('direktor/update_student', user_login.UPDATESTUDENT, name='update_student'),
    path('direktor/delete_student/<str:id>', user_login.DELETESTUDENT, name='delete_student'),

    path('direktor/course/add_course', user_login.ADDCOURSE, name='add_course'),
    path('direktor/course/view_course', user_login.VIEWCOURSE, name='view_course'),
    path('direktor/course/edit_course<str:id>', user_login.EDITCOURSE, name='edit_course'),

    path('direktor/add_session', user_login.ADDSESSION, name='add_session'),
    path('direktor/view_session', user_login.VIEWSESSION, name='view_session'),
    path('direktor/edit_session<str:id>', user_login.EDITSESSION, name='edit_session'),
    path('direktor/update_session', user_login.UPDATESESSION, name='update_session'),
    path('direktor/delete_session<str:id>', user_login.DELETESESSION, name='delete_session'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
