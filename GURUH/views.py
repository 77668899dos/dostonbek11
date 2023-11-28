from django.shortcuts import redirect,render

def BASE(request):
    return render(request,'base.html')

def HOME(request):
    return  render(request, 'Main/home.html')

def ABOUT(request):
    return  render(request, 'Main/about.html')

