from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms.widgets import HiddenInput

from authapp.models import ShopUser
from mainapp.models import Category, Product


class RegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ("username",)


class UserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ("username", "first_name", "last_name", "image", "email", "city")


class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].widget = HiddenInput()
