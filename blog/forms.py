from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        widgets = {
                'user_name': forms.TextInput(attrs={
                    'class': 'user-name-field',
                    'placeholder': 'Your Name'
                }),

                'comment': forms.Textarea(attrs={
                    'class': 'comment-field',
                    'placeholder': 'Leave a comment...'
                })
                }
