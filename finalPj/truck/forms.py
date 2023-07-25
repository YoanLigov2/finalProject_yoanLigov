from django import forms
from .models import Truck


class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        exclude = ('user', )
        labels = {
            'truck_mass': "Truck Mass(in tons)",
            'truck_height': "Truck Height(in meters)",
            'engine_power': "Engine Power(in horse power)",
            'very_short_description': 'Very Short Description(Optional)'
        }


class TruckDeleteForm(TruckForm):

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
