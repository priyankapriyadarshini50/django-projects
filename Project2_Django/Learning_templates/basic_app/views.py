from django.shortcuts import render


# Create your views here.
def index(request):
    content_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'basic_app/index.html', context=content_dict)


def other(request):
    content_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'basic_app/other.html', context=content_dict)


def relative_url(request):
    return render(request, 'basic_app/relative_url_template.html', context=None)


def thankyou(request):
    my_dict = {'text_input': 'this is developed by priyanka'}
    return render(request, 'basic_app/thank_you.html', context=my_dict)
