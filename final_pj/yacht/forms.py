from django import forms
from .models import Yacht


class YachtForm(forms.ModelForm):
    class Meta:
        model = Yacht
        exclude = ('user', )
        labels = {
            'yacht_length': "Yacht Length(in meters)",
            'very_short_description': 'Very Short Description(Optional)',
            'price': 'Price in Bulgarian leva'
        }


class YachtDeleteForm(YachtForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False