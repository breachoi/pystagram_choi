from django import forms
from posts.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
            "post",
        ]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "write comment...",
                }
            )
        }