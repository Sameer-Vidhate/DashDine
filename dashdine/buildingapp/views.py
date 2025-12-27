from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Welcome to DashDine")
    return render(request, 'index.html')

def sign_up(request):
    return render(request, 'sign-up.html')

def sign_in(request):
    return render(request, 'sign-in.html')

def choice_page(request):
    return render(request, 'choice_page.html')

def open_sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        return HttpResponse(f"Your Sign-Up is Successful {username}.")
    else:
        return HttpResponse("Invalid Response")

#def open_sign_in(request):
