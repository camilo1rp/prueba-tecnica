from django import forms

from .models import Contacts


class ContactForm(forms.ModelForm):
    """Form for adding new contact"""

    def __init__(self, *args, **kwargs):
        states = kwargs.pop('state')
        super().__init__(*args, **kwargs)
        self.fields['state'] = forms.ChoiceField(label="Departamento*",choices=zip(states, states))
        self.fields['city'] = forms.CharField(label="Ciudad*",widget=forms.Select)
        self.fields['email'].label = "Correo*"
        self.fields['name'].label = "Nombre*"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"

    class Meta:
        model = Contacts
        fields = ['name', 'state', 'city', 'email']
