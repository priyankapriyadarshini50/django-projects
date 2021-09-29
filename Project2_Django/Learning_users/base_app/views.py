from django.shortcuts import render
from base_app.forms import UserForm, UserProfileInfoForm
from base_app.models import UserProfileInfo


# import for login view
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'base_app/index.html', context=None)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    #user_profile_obj = UserProfileInfo.objects.get("id")
    #user_dict = {'user_data': user_profile_obj}
    return render(request, 'base_app/special.html', context=None)
    # HttpResponse("You have logged in, Nice")


def register(request):
    # the new user has not registered yet and it is used in template tagging in registration.html
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            # the save() creates a new entry using the input data and saves it to the database
            new_user_entry = user_form.save()
            # it changed the raw password to hash code
            new_user_entry.set_password(new_user_entry.password)
            new_user_entry.save()

            # Below it ust creates a new entry, but has not saved to db
            new_profile_entry = profile_form.save(commit=False)
            # below defines the one to one relationship between UserInfoProfile and User
            # here we have assigned the (username, password and email field data to user
            # field of UserInfoProfile model/UserInfoProfileForm)
            new_profile_entry.user = new_user_entry

            if 'profile_pic' in request.FILES:
                # retrieve the profile pic from request.Files and assigned to profile_pic field of new_profile_entry
                new_profile_entry.profile_pic = request.FILES['profile_pic']

            new_profile_entry.save()
            registered = True
            return HttpResponseRedirect(reverse('base_app:login'))

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    form_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render(request, 'base_app/registration.html', context=form_dict)


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST["username"]
        pass_word = request.POST["password"]
        print(user_name, pass_word)

        # if authenticated, returns a User object(entry/row), otherwise it returns None
        user_auth = authenticate(username=user_name, password=pass_word)
        print(user_auth)
        print(user_auth.is_authenticated)

        if user_auth is not None:
            # is_active is a field in User Model(table), so do not use it as a method
            # do not use parenthesis()
            if user_auth.is_active:
                login(request, user_auth)
                print("User has successfully logged in")
                return HttpResponseRedirect(reverse('special'))
            else:
                return HttpResponse("ACCOUNT IS NOT ACTIVE")

        else:
            print("Someone tried to login and failed")
            print("Username: ", user_name)
            print("Password: ", pass_word)
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request, 'base_app/login.html', context=None)









