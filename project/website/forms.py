from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import *


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request = ..., *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Введите вашу электронную почту'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Введите ваш пароль'})
    
    class Meta:
        model = CustomUser
        fields = {
            'username': _('Электронная почта'),
            'password': _('Пароль')
        }