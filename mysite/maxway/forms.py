from .models import *
from django import forms


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category()
        fields = ['name', 'combo']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product()
        fields = ['title', 'description', 'image', 'price', 'foods', 'category']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order()
        fields = ['total_price', 'status']


class DelilveryinfoForm(forms.ModelForm):
    class Meta:
        model = Delilveryinfo()
        fields = ['order', 'first_name', 'last_name', 'phone_number', 'payment_type', 'address']