from django import forms
from .models import CommentPost


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ['content']


class LoginForm(forms.Form):
    class Meta:
        username = forms.CharField(max_length=100)
        password = forms.PasswordInput()



