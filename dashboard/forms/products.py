from django import forms
from medical.models import (
    ProductCategory,
    Product,
    ProductFeature,
    ProductImage,
    ProductReview,
)


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ["name", "slug"]


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
            "old_price",
            "country",
            "certificates",
            "stock_status",
            "rating",
            "reviews_count",
        ]


class ProductFeatureForm(forms.ModelForm):
    class Meta:
        model = ProductFeature
        fields = ["icon", "title", "description"]


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ["product", "image"]


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ["product", "reviewer", "rating", "comment"]
