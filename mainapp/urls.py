from django.urls import path
from . import views
from .views import products, product

app_name = 'mainapp'

urlpatterns = [
    path('', views.products, name='products'),
    path('product/<int:pk>/', product, name='product'),
    path('category/<int:pk>/', products, name='category'),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
]
