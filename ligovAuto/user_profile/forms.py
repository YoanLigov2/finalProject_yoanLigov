from django.contrib.auth.forms import UserCreationForm
from .models import CollectionUser
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class CollectionUserCreationForm(UserCreationForm):
    class Meta:
        model = CollectionUser
        fields = ('username', 'email', 'phone_number')


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current_password', 'placeholder': 'Password'})
    )


class CollectionUserEditForm(forms.ModelForm):
    class Meta:
        model = CollectionUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'profile_picture',
            'gender',
            'phone_number',
        )
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'profile_picture': 'Image',
            'gender': 'Gender',
            'phone_number': 'Phone Number'
        }