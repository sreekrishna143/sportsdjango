from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
import time,datetime,pyqrcode
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import get_user_model
from django.db import connection
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Player, Feedback
from .forms import PlayerForm
# from .forms import EditProfileForm


def function1(request):
    if request.user.is_authenticated:
        context = {'user_name': request.user.first_name}
    else:
        context = {}
    return render(request, "index.html", context)

def function2(request):
    return render(request,"matches.html")
def function3(request):
    return render(request,"players.html")
def function4(request):
    return render(request,"blog.html")
def function5(request):
    return render(request,"contact.html")
def function6(request):
    return render(request,"index.html")
def function7(request):
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        dob = request.POST['dob']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        address = request.POST['address']

        User = get_user_model()

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already registered')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )
                user.first_name = full_name
                user.dob = dob
                user.gender = gender
                user.phone_number = phone_number
                user.address = address
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'index.html')


# Sign In view
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')  # Redirect to a home or dashboard page
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def profile(request):
    # Get the logged-in user
    user = request.user

    if user.dob:
        today = datetime.today()
        age = today.year - user.dob.year - ((today.month, today.day) < (user.dob.month, user.dob.day))
    else:
        age = None  # If the DOB is not set

    # Prepare user data
    user_data = {
        'full_name': user.first_name,  # Assuming `first_name` stores the full name
        'age': age,
        'email': user.email,
        'dob': user.dob,
        'gender': user.gender,
        'phone_number': user.phone_number,
        'address': user.address,
        'goals': user.goals if hasattr(user, 'goals') else 0,
        'wins': user.wins if hasattr(user, 'wins') else 0,
        'matches': user.matches if hasattr(user, 'matches') else 0,
        'draws': user.draws if hasattr(user, 'draws') else 0,
    }

    return render(request, 'profile.html', {'user_data': user_data})


def player_list(request):
    players = Player.objects.all()
    countries = sorted(set(players.values_list('country', flat=True)))
    grouped_players = {country: players.filter(country=country) for country in countries}
    return render(request, 'players.html', {'grouped_players': grouped_players})

def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('players')
    else:
        form = PlayerForm()
    return render(request, 'add_player.html', {'form': form})

def feedbackpagecall(request):
    return render(request, 'feedback_form.html')

def ticketbookingpagecall(request):
    return render(request, 'ticketbooking.html')

def feedbacklogic(request):
    if request.method == 'POST':
        username = request.POST.get('feedname')
        email = request.POST.get('feedemail')
        feedback_text = request.POST.get('feedback')

        print(username, email, feedback_text)  # Debug: print to console

        # Save to database
        Feedback.objects.create(username=username, email=email, feedback=feedback_text)
        return redirect('feedbackpagecall')

    return render(request, 'feedback_form.html')


# Logout view
def logout(request):
    auth.logout(request)
    return redirect('home')
