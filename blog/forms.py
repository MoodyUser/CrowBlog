from django import forms
from blog.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post


class ContactUsForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    content = forms.CharField(widget=forms.Textarea())
