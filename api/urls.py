from django.urls import path
from .views import CustomUserView,StudentView


urlpatterns = [
    path('',CustomUserView.as_view()),
    path('<int:pk>/',StudentView.as_view()),
]