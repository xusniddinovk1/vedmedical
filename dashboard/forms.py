from django import forms
from medical.models import (
    Category,
    Product,
    Service,
    News,
    Partner,
    GalleryImage,
    CompanyInfo,
)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'icon']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kategoriya nomi'}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'FontAwesome ikonka'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'category', 'description', 'short_description',
            'image', 'price', 'composition', 'dosage', 'manufacturer', 'image'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'short_description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'composition': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'dosage': forms.TextInput(attrs={'class': 'form-control'}),
            'manufacturer': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'onchange': 'loadFile(event)'}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'icon', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'icon': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'excerpt', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        }


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['logo', 'website']
        widgets = {
            'website': forms.URLInput(attrs={'class': 'form-control'}),
        }


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['image']


class CompanyInfoForm(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        fields = [
            'company_name', 'about_us', 'mission', 'phone', 'email',
            'address', 'facebook_url', 'instagram_url', 'telegram_url',
            'youtube_url', 'logo', 'image'
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'about_us': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'mission': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'facebook_url': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control'}),
            'telegram_url': forms.URLInput(attrs={'class': 'form-control'}),
            'youtube_url': forms.URLInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control', 'onchange': 'loadFile(event)'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'onchange': 'loadFile(event)'}),
        }
