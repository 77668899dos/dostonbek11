from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from app.models import CustomUser,Student
from .serializers import CustomUserSerializer, StudentSerializer

class CustomUserView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class StudentView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

