from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('brend/<slug:brend_slug>/', views.product_list, name='product_list_by_brend'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
