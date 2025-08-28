from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', main_dashboard, name='main_dashboard'),
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),
    # ---------------- CATEGORY ----------------
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # ---------------- PRODUCT ----------------
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),

    # ---------------- SERVICE ----------------
    path('services/', views.service_list, name='service_list'),
    path('services/create/', views.service_create, name='service_create'),
    path('services/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),

    # ---------------- NEWS ----------------
    path('news/', views.news_list, name='news_list'),
    path('news/create/', views.news_create, name='news_create'),
    path('news/<int:pk>/edit/', views.news_edit, name='news_edit'),
    path('news/<int:pk>/delete/', views.news_delete, name='news_delete'),

    # ---------------- PARTNER ----------------
    path('partners/', views.partner_list, name='partner_list'),
    path('partners/create/', views.partner_create, name='partner_create'),
    path('partners/<int:pk>/edit/', views.partner_edit, name='partner_edit'),
    path('partners/<int:pk>/delete/', views.partner_delete, name='partner_delete'),

    # ---------------- GALLERY ----------------
    path('gallery/', views.gallery_list, name='gallery_list'),
    path('gallery/create/', views.gallery_create, name='gallery_create'),
    path('gallery/<int:pk>/delete/', views.gallery_delete, name='gallery_delete'),

    # ---------------- COMPANY INFO ----------------
    path('company-info/', views.company_info_view, name='company_info'),
]
