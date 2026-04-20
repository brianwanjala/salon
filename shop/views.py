from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Service
from django.contrib.auth.decorators import login_required
from .booking import BookingForm

# Create your views here.
def home(request):
    services = Service.objects.all()
    return render(request, 'shop/index.html', {'services': services})
def about(request):
    return render(request, 'shop/about.html')
def services(request):
    return render(request, 'shop/services.html')
def gallery(request):
    return render(request, 'shop/portfolio.html')
def blog(request):
    return render(request, 'shop/blog.html')
def contact(request):
    return render(request, 'shop/contact.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'shop/login.html', {'error': 'Invalid credentials'})

    return render(request, 'shop/login.html')

from django.contrib import messages

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user

            try:
                booking.full_clean()  
                booking.save()
                messages.success(request, "Booking successful!")
                return redirect('home')
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = BookingForm()

    return render(request, 'shop/book.html', {'form': form})