from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from .models import Post, Comment
from .forms import PostForm, CommentForm, UserForm, UserInfoForm


# Create your views here.
class AboutTemplateView(TemplateView):
    template_name = 'blog/about.html'


class PostListView(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'

    # __lte(means less than equal to)
    # _publish_date means recent posts display on the top
    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post_detail'


class PostCreateView(CreateView, LoginRequiredMixin):
    # to create a post user has to log in to the site
    # If a view is using this mixin, all requests by non-authenticated users will be redirected to the login page
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'


class PostUpdateView(UpdateView, LoginRequiredMixin):
    # If a view is using this mixin, all requests by non-authenticated users will be redirected to the login page
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'


class PostDeleteView(DeleteView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(ListView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull=True).order_by('create_date')


################################################################
# FUNCTION BASED VIEWS FOR COMMENT
################################################################
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # the post object is calling to publish() which is defined in the models.py
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def add_comment_to_post(request, pk):
    # get the post object/record which has pk=pk from Post model
    # if it does not exist, return 404 object
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # validate the input
        if form.is_valid():
            comment = form.save(commit=False)
            # before saving to db, comment object/record has post attribute/field
            # in the post field we are saving the post object(linked with ForeignKey)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    form_dict = {'form': form}
    render(request, 'blog/post_detail.html', context=form_dict)


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    # before deleting we need to save the pk for that post
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


###########################################
# Function Based View for User Registration
##########################################
def user_registration(request):
    # registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_info_form = UserInfoForm(request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user_entry = user_form.save()
            # save encrypted/hasher password
            user_entry.set_password(user_entry.password)
            # save all the cleaned values to db
            user_entry.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user_entry
            user_info.save()
            # registered = True
            return HttpResponseRedirect(reverse('login'))
        else:
            print(user_form.errors, user_info_form.errors)

    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()

    form_dict = {'user_form': user_form, 'user_info': user_info_form}
    return render(request, 'registration/signup.html', context=form_dict)


def user_login(request):
    if request.method == 'POST':
        # user input data
        print(request.POST)
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        print(user_name)

        # authenticate the user by comparing the database username and password with input username password
        user_auth = authenticate(username=user_name, password=pass_word)
        print(user_auth)
        # print(user_auth.is_authenticated)

        if user_auth is not None:
            # is_active ia an User attribute which contains boolean value(True/False)
            if user_auth.is_active:
                login(request, user_auth)
                print("User has successfully logged in")
                return redirect('post_list')
        else:
            print("Someone is trying to login and failed")

    return render(request,'registration/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')






