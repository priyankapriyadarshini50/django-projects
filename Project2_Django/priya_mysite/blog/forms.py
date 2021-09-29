from django import forms
from .models import Post, Comment, UserInfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'textinputclass'}),
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(attrs={'class': 'textinputclass' }),
        }


class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ('gender', 'date_of_birth')

        widgets = {
            'gender': forms.RadioSelect(),
            'date_of_birth': forms.DateInput(format='%d/%m/%Y'),
        }


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'designation')

        # if i want to provide style to some fields then we need to put them in the widgets
        # and assign them some class. so that we can use those classes to give styling in the .css file
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'designation': forms.RadioSelect(),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('random_author', 'text')

        widgets = {
            'random_author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
