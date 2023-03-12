from .models import Comment
from django import forms
from taggit.forms import TagField
from taggit_labels.widgets import LabelWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'comment',
        )
