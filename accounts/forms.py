from django import forms
from accounts.models import Details,Items
class Detailsform(forms.ModelForm):

    class Meta():
        model=Details
        fields=('branch','semester')

class ItemCreateForm(forms.ModelForm):

    class Meta():
        model=Items
        fields=('name','category')
