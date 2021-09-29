from django.shortcuts import render
from second_app.models import UserInfo
from second_app.forms import UserInfoForm


# Create your views here.
def index(request):
    my_dict = {'insert_content':'This is a dynamic content and template variable'}
    return render(request, 'second_app/index.html', context=my_dict)


def user_info(request):
    user_info_rec = UserInfo.objects.all()
    user_info_dict = {'userinfo_record': user_info_rec}
    return render(request, 'second_app/userinfo.html', context=user_info_dict)


def signup(request):
    if request.method == 'POST':
        form_obj = UserInfoForm(request.POST)

        if form_obj.is_valid():
            print("data validation completed")
            form_obj.save()
            return thank_you(request)
    else:
        form_obj = UserInfoForm()

    form_dict = {"form": form_obj}
    return render(request, 'second_app/sign_up.html', context=form_dict)


def thank_you(request):
    # get all the entries/row objects from model
    user_obj = UserInfo.objects.all()
    # convert it to a list
    user_obj_list = list(user_obj)
    # get the last entered row so index is -1
    # UserInfo model class return full name in __str__(self)
    print(user_obj_list[-1])
    latest_user_dict = {'latest_user': user_obj_list[-1]}
    return render(request, 'second_app/thank_you.html', context=latest_user_dict)


# different way to get the first name and last name of the latest user
# def thankYou(request):
    # f_name_list = UsersInfo.objects.all().last()
    # f_name = UserInfo.objects.values_list('first_name')
    # f_name_list = list(f_name)
    # l_name = UserInfo.objects.values_list('last_name')
    # l_name_list = list(l_name)
    # newly_entered_full_name = ' '.join(f_name_list[-1]+l_name_list[-1])
    # user_fullname = {'insert_fullname': newly_entered_full_name}
    # return render(request, 'AppTwo_template/thank_you.html', context=user_fullname)


