from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, WebPage


# Create your views here.
def index(request):
    webpg_list = AccessRecord.objects.order_by('date')
    topics = WebPage.objects.all()
    webpg_dict = {'access_rec': webpg_list, "topics": topics}
    return render(request, 'first_app_temp/index.html', context=webpg_dict)
