from django import forms
from discussion_forum.models import Comments,Thread
class ThreadForm(forms.ModelForm):

    class Meta():
        model=Thread
        fields=('name','description')

class CommentForm(forms.ModelForm):

    class Meta():
        model=Comments
        fields=('comment',)
