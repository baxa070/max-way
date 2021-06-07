from django import forms
from maxway.models import *


class DelilveryinfoForm(forms.ModelForm):
    class Meta:
        model = Delilveryinfo()
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order()
        fields = "__all__"


class OrdForm(forms.ModelForm):
    class Meta:
        model = Order()
        fields = ('status',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category()
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product()
        fields = "__all__"
