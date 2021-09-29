from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from .models import School, Student
from django.urls import reverse_lazy


class TBView(TemplateView):
    template_name = 'cbs_app/index.html'

    # now i want to inject some content to my template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Here we will provide the key/value pair dictionary content
        context['injected'] = 'INJECTED FROM CLASS BASED TEMPLATE VIEW'
        context['new_injected'] = 'This is a new injected value from TemplateView'
        return context


# FUNCTION BASED VIEW
def cbs_home(request):
    home_dict = {'injected': 'Injected from function based view',
                 'new_injected':'This is a new injected value from FBV'}
    return render(request, 'cbs_app/index.html', context=home_dict)


# it will display the list of school objects/entry/record and returns a school_list
# it extract data from database models and display as a list
class SchoolListView(ListView):
    # context_object_name returns all the objects/entries from the school models
    # we can also use get_queryset() to retrieve particular data from school model
    def get_queryset(self):
        return School.objects.order_by('name')

    context_object_name = 'schools'
    model = School
    template_name = 'basic_app/school_list.html'


# FUNCTION BASED VIEW IMPLEMENTATION
def schools_list(request):
    school_obj_list = School.objects.order_by('name')
    school_dict = {'inserted_schools': school_obj_list}
    return render(request, 'basic_app/school_list.html', context=school_dict)


# it will display the list of school objects/entry(parent class) and associated Student(subclass) objects
# it extract data from database models and display as a details view with pk
class SchoolDetailView(DetailView):

    context_object_name = 'school_detail'
    model = School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    model = School
    fields = ('name', 'principal', 'location')
    template_name = 'basic_app/school_form.html'


class SchoolUpdateView(UpdateView):
    model = School
    fields = ('name', 'principal')
    template_name = 'basic_app/school_form.html'


class SchoolDeleteView(DeleteView):
    model = School
    template_name = 'basic_app/school_confirm_delete.html'
    success_url = reverse_lazy('cbs_app:list')





