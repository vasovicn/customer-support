from django.shortcuts import render, redirect
from .models import Ticket
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from datetime import datetime


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


def support(request):
    if request.method=='POST':
        name = request.POST['name']
        number = request.POST['number']
        company = request.POST['company']
        email = request.POST['email']
        subject = request.POST['subject']
        problem = request.POST['problem']
        dateetime = request.POST['datetime']
        if dateetime == '':
            dateandtime = None
        else:
            #Converting string variable dateetime in datetime format
            datetime_obj = datetime.strptime(dateetime, "%Y-%m-%dT%H:%M")
            a = datetime_obj.time()
            b = a.hour + a.minute/100
            #If weekday is Sunday
            if datetime_obj.weekday() == 6:
                messages.info(request, 'Date and time for callback cannot be Sunday')
                return redirect('support')
            #If weekday is Saturday
            elif datetime_obj.weekday() == 5:
                if b < 8.00 or b > 13.00:
                    messages.info(request, 'Time for callback on Saturdays is betwen 08:00 and 13:00')
                    return redirect('support')
            #If weekday is workday
            else:
                if b < 8.00 or b > 20.00:
                    messages.info(request, 'Time for callback on weekdays is betwen 08:00 and 20:00')
                    return redirect('support')
            dateandtime = request.POST['datetime']
        #Checking if input number is numeric
        num = number.isnumeric()
        if num == False:
            messages.info(request, 'Phone number must be numeric')
            return redirect('support')
        ticket = Ticket(name=name, number=number, company=company, email=email, subject=subject, problem=problem, date_and_time_for_callback=dateandtime, comment=None)
        ticket.save()
        messages.add_message(request, messages.SUCCESS,  '✔ Your ticket has been submitted successfully!')
        return redirect('homepage')
    else:
        return render(request, 'support.html')


def register(request):
    '''Getting data from html form and checking: if password is same ass repeated password
                                                 if username is already exist
                                                 if email is already exist'''
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_rp = request.POST['password2']
        if password == password_rp:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already exist')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=name)
                user.save()
                messages.add_message(request, messages.SUCCESS, 'You have successfully created account')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    '''Getting data from html form for username and password and authenticating credentials'''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'You have successfully logged in')
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("homepage")