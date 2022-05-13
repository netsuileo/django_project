import basketapp.views as basketapp
from django.urls import path

app_name = "basketapp"

urlpatterns = [
    path("", basketapp.view, name="view"),
    path("add/<int:product_id>", basketapp.add, name="add"),
    path("remove/<int:basket_id>", basketapp.remove, name="remove"),
]
