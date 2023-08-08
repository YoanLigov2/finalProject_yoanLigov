from django import forms
from .models import Motorbike


class MotorbikeForm(forms.ModelForm):
    class Meta:
        model = Motorbike
        exclude = ('user',)
        labels = {
            'bike_type': "Type",
            'engine_size': "Engine Size(in cc)",
            'fuel_capacity': "Fuel Capacity(in liters)",
            'top_speed': "Top Speed(in kilometers)",
            'short_description': 'Short Description(Optional)',
            'price': 'Price in Bulgarian leva'
        }


class MotorbikeDeleteForm(MotorbikeForm):

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
