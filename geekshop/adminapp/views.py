from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from adminapp.forms import (CategoryEditForm, ProductEditForm, RegisterForm,
                            UserEditForm)
from authapp.models import ShopUser
from mainapp.models import Category, Product
from utils.decorators import check_is_superuser
from utils.mixins import SuperuserRequiredMixin, TitleMixin


class UserListView(SuperuserRequiredMixin, TitleMixin, ListView):
    template_name = "adminapp/users.html"
    model = ShopUser
    title = "Пользователи"
    paginate_by = 4
    page_kwarg = "my_page"

    def get_queryset(self):
        return ShopUser.objects.order_by("date_joined")


class UserCreateView(SuperuserRequiredMixin, TitleMixin, CreateView):
    template_name = "adminapp/create_user.html"
    model = ShopUser
    form_class = RegisterForm
    success_url = reverse_lazy("admin:users")
    title = "Создание пользователя"


class UserUpdateView(SuperuserRequiredMixin, TitleMixin, UpdateView):
    template_name = "adminapp/update_user.html"
    model = ShopUser
    form_class = UserEditForm
    success_url = reverse_lazy("admin:users")
    title = "Редактирование пользователя"


@check_is_superuser
def delete_user(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse("admin:users"))


class CategoryListView(SuperuserRequiredMixin, TitleMixin, ListView):
    template_name = "adminapp/categories.html"
    model = Category
    title = "Категории"


@check_is_superuser
def create_category(request):
    form = CategoryEditForm()
    if request.method == "POST":
        form = CategoryEditForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("admin:categories"))

    return render(
        request,
        "adminapp/create_category.html",
        context={"title": "Создание категории", "form": form},
    )


@check_is_superuser
def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryEditForm(instance=category)
    if request.method == "POST":
        form = CategoryEditForm(instance=category, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("admin:categories"))

    return render(
        request,
        "adminapp/update_category.html",
        context={
            "title": "Редактирование категории",
            "category": category,
            "form": form,
        },
    )


@check_is_superuser
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.is_active = False
    category.save()
    return HttpResponseRedirect(reverse("admin:categories"))


@check_is_superuser
def products(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    return render(
        request,
        "adminapp/products.html",
        context={
            "title": f"Категория: {category.name}",
            "products": Product.objects.filter(category=category),
            "category": category,
        },
    )


@check_is_superuser
def create_product(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    form = ProductEditForm(initial={"category": category})
    if request.method == "POST":
        form = ProductEditForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("admin:products", args=[category_pk]))

    return render(
        request,
        "adminapp/create_product.html",
        context={"title": "Создание продукта", "category": category, "form": form},
    )


@check_is_superuser
def update_product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    form = ProductEditForm(instance=product)
    if request.method == "POST":
        form = ProductEditForm(instance=product, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse("admin:products", args=[product.category.pk])
            )

    return render(
        request,
        "adminapp/update_product.html",
        context={"title": "Редактирование категории", "product": product, "form": form},
    )


@check_is_superuser
def delete_product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    product.is_active = False
    product.save()
    return HttpResponseRedirect(reverse("admin:products", args=[product.category.pk]))
