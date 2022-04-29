from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from authapp.models import ShopUser


class LoginForm(AuthenticationForm):
    pass


class RegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ("username",)


class UserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ("username", "first_name", "last_name", "image", "email", "city")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "password":
                field.widget = forms.HiddenInput()

    def clean_city(self):
        if self.cleaned_data["city"] != "Владикавказ":
            raise forms.ValidationError("Мы работаем только во Владикавказе.")

        return self.cleaned_data
