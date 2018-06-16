from django import forms
from .models import Shortly

class ShortlyForm(forms.ModelForm):
    class Meta:
        model = Shortly
        fields = ('link',)
    

