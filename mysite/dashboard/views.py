from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import service
from maxway.forms import (ProductForm, OrderForm, CategoryForm, DelilveryinfoForm)
from maxway.models import *


def login_required_decorator(f):
    return login_required(f, login_url="login")


@login_required_decorator
def dashboard_page(request):
    status = service.get_status_info([1, 2, 3])
    count_cat = service.get_category_count()['name']
    count_prod = service.get_product_count()['title']
    categories = service.news_count()
    status_1 = service.get_status_1()[0]['count']
    status_2 = service.get_status_2()[0]['count']
    status_3 = service.get_status_3()[0]['count']

    bar_status = {
        "order": status_1,
        "done": status_2,
        "failed": status_3,
    }

    ctx = {
        "count_cat": count_cat,
        "count_prod": count_prod,
        "categories": categories,
        "status": status,
        "bars": bar_status,

    }
    return render(request, 'dashboard/index.html', ctx)


@login_required_decorator
def status(request, pk, status):
    model = Order.objects.get(id=pk)
    model.status = status
    model.save()

    return redirect('order_list')


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


@login_required_decorator
def dashboard_logout(request):
    logout(request)
    return redirect('login')


@login_required_decorator
def order_list(request):
    status = service.get_status_info([1, 2, 3])
    filter = "all"
    if request.POST:
        filter = request.POST.get("order_filter")

        if filter == "done":
            status = service.get_status_info([2])

        if filter == "failed":
            status = service.get_status_info([3])

    ctx = {
        "status": status,
        "filter": filter,
    }
    return render(request, 'dashboard/order/lilst.html', ctx)


@login_required_decorator
def user_list(request):
    users = service.get_user()
    ctx = {
        "users": users
    }
    return render(request, 'dashboard/user/list.html', ctx)


@login_required_decorator
def user_create(request):
    model = Delilveryinfo()
    form = DelilveryinfoForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('user_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/user/form.html', ctx)


@login_required_decorator
def user_edit(request, pk):
    model = Delilveryinfo.objects.get(id=pk)
    form = DelilveryinfoForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('user_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/user/form.html', ctx)


@login_required_decorator
def user_delete(request, pk):
    model = Delilveryinfo.objects.get(id=pk)
    model.delete()
    return redirect('user_list')


@login_required_decorator
def category_list(request):
    categories = service.get_category()
    ctx = {
        "categories": categories
    }
    return render(request, 'dashboard/category/list.html', ctx)


@login_required_decorator
def category_create(request):
    model = Category()
    form = CategoryForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


@login_required_decorator
def category_edit(request, pk):
    model = Category.objects.get(id=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


@login_required_decorator
def category_delete(request, pk):
    model = Category.objects.get(id=pk)
    model.delete()
    return redirect('category_list')


@login_required_decorator
def product_list(request):
    products = service.get_product()
    ctx = {
        "products": products
    }
    return render(request, 'dashboard/product/list.html', ctx)


@login_required_decorator
def product_create(request):
    model = Product()
    form = ProductForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/product/form.html', ctx)


@login_required_decorator
def product_edit(request, pk):
    model = Product.objects.get(id=pk)
    form = ProductForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/product/form.html', ctx)


@login_required_decorator
def product_delete(request, pk):
    model = Product.objects.get(id=pk)
    model.delete()
    return redirect('product_list')