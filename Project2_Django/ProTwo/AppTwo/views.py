from django.shortcuts import render
# from django.http import HttpResponseRedirect
from AppTwo.models import UsersInformation
from AppTwo.forms import UserNewForm


# Create your views here.
def home(request):
    my_home = {'insert_home': "Go to users/ to get the users information.."}
    return render(request, 'AppTwo_template/home.html', context=my_home)


def user_signup(request):
    if request.method == 'POST':
        form = UserNewForm(request.POST)

        if form.is_valid():
            print("Data entry is successfull")
            form.save(commit=True)
            return thankYou(request)
    else:
        form = UserNewForm()
    form_dict = {'form': form}
    return render(request, 'AppTwo_template/Sign_up.html', context=form_dict)


def usersInfo(request):
    info_list = UsersInformation.objects.order_by('first_name')
    print(info_list)
    info_dict = {'access_userinfo': info_list}
    return render(request, 'AppTwo_template/usersInfo.html', context=info_dict)


def thankYou(request):
    #f_name_list = UsersInfo.objects.all().last()
    f_name = UsersInformation.objects.values_list('first_name')
    f_name_list = list(f_name)
    print(f_name_list)

    l_name = UsersInformation.objects.values_list('last_name')
    l_name_list = list(l_name)
    newly_entered_full_name = ' '.join(f_name_list[-1]+l_name_list[-1])
    user_fullname = {'insert_fullname': newly_entered_full_name}
    return render(request, 'AppTwo_template/thank_you.html', context=user_fullname)

