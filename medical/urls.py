from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path("about/", views.about, name="about"),
    path("manufacturing/", views.manufacturing_page, name="manufacturing"),
    path("partners/", views.partners_page, name="partners"),
    path("galleries/", views.gallery_page, name="gallery"),
    path("products/", views.product_list, name="products"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("news/", views.news_list, name="news"),
]
