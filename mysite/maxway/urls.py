from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name="home-page"),
    path('order/', views.order_page, name="order-page"),
    path('order/save/', views.order_save, name="order-save"),
]