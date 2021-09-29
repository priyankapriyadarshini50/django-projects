from django.shortcuts import render
from . import forms


# Create your views here.
def index(request):
    my_index = {'insert_info': "Go to next form page to fill out the form."}
    return render(request, 'third_app_temp/index.html', context=my_index)


def form_name_view(request):

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        # print(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            print("Name: ", form.cleaned_data['name'])
            print("Email: ", form.cleaned_data['email'])
            print("Text: ", form.cleaned_data['text'])
            return index(request)

    else:
        form = forms.FormName()

    form_dict = {'form': form}
    # print("Errors:", form.errors)
    return render(request, 'third_app_temp/form_basic.html', context=form_dict)


def image_view(request):
    return render(request, 'third_app_temp/image.html', context=None)
