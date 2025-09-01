from django import forms
from medical.models import (
    ProductCategory,
    Product,
    ProductFeature,
    ProductImage,
)


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ["name"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "category",
            "title",
            "description",
            "image",
            "badge",
            "specs",
            "price",
            "country",
            "certificates",
        ]


class ProductFeatureForm(forms.ModelForm):
    class Meta:
        model = ProductFeature
        fields = ["icon", "title", "description"]


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ["product", "image"]
