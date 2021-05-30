from django.shortcuts import render
from.models import *


def home(request):
	category = Category.objects.all()
	product = Product.objects.all()
	order = Order.objects.all()
	deleveryinfo = Delilveryinfo.objects.all()
	ctx = {
		"category": category,
		"product": product,
		"order": order,
		"deleveryinfo": deleveryinfo
	}
	return render(request, 'index.html')


def order(request):
	category = Category.objects.all()
	product = Product.objects.all()
	order = Order.objects.all()
	deleveryinfo = Delilveryinfo.objects.all()
	ctx = {
		"category": category,
		"product": product,
		"order": order,
		"deleveryinfo": deleveryinfo
	}
	return render(request, 'order.html', ctx)