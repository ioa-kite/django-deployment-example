from django.shortcuts import render
from ProFive_app.forms import UserForm, UserProfileInfoForm
from ProFive_app.models import User, UserProfileInfo
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    return render(request, 'ProFive_app/index.html')



def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        userProfile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and userProfile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = userProfile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors, userProfile_form.errors)
    else:
        user_form = UserForm()
        userProfile_form = UserProfileInfoForm()

    return render(request, 'ProFive_app/registration.html',
                  {'registered': registered, 'user_form': user_form, 'profile_form': userProfile_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print("someone tried to login and failed")
            print('Username {} and PW {}'.format(username, password))
    else:
        return render(request, 'ProFive_app/login.html', {})


@login_required
def special(request):
    return HttpResponse('Hey youre logged in ! Yo')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
