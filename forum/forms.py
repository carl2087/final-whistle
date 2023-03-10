from .models import Comment
from django import forms
from taggit.forms import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'comment',
            'tags',
        )
        widgets = {
            'tags': TagWidget(),
        }
