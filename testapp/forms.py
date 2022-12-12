from django.contrib.auth.forms import UserCreationForm

from .models import TestUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = TestUser
        fields = ('username', 'password1', 'password2', 'email')

