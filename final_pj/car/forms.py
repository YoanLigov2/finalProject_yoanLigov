from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('user', )
        labels = {
            'car_type': "Type",
            'image': "Image",
            'top_speed': "Top Speed(in kilometers)",
            'short_description': "Short Description(Optional)",
            'price': 'Price in Bulgarian leva'
        }


class CarDeleteForm(CarForm):

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
