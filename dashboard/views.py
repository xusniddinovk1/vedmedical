from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from medical.models import Category, Product, Service, News, Partner, GalleryImage, CompanyInfo
from .forms import (
    CategoryForm, ProductForm, ServiceForm, NewsForm,
    PartnerForm, GalleryImageForm, CompanyInfoForm
)


def login_required_decorator(func):
    return login_required(func, login_url="login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main_dashboard")
    return render(request, "dashboard/login.html")


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def main_dashboard(request):
    categories = Category.objects.all()[:6]  # 6 ta kategoriya
    products = Product.objects.all()[:8]  # 8 ta mahsulot
    services = Service.objects.all()[:6]  # 6 ta xizmat
    news_list = News.objects.all()[:3]  # 3 ta yangilik
    partners = Partner.objects.all()
    gallery = GalleryImage.objects.all()[:6]  # 6 ta galereya rasmi
    company = CompanyInfo.objects.first()  # bitta company info

    context = {
        'categories': categories,
        'products': products,
        'services': services,
        'news_list': news_list,
        'partners': partners,
        'gallery': gallery,
        'company': company,
    }
    return render(request, 'dashboard/index.html', context)


# -------------------- CATEGORY --------------------
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/list.html', {'categories': categories})


def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Kategoriya qo‘shildi ✅")
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category/form.html', {'form': form})


def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Kategoriya yangilandi ✏️")
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/form.html', {'form': form})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.delete()
        messages.success(request, "Kategoriya o‘chirildi ❌")
        return redirect('category_list')
    return render(request, 'category/confirm_delete.html', {'object': category})


# -------------------- PRODUCT --------------------
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/list.html', {'products': products})


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Mahsulot qo‘shildi ✅")
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product/form.html', {'form': form})


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Mahsulot yangilandi ✏️")
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/form.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Mahsulot o‘chirildi ❌")
        return redirect('product_list')
    return render(request, 'product/confirm_delete.html', {'object': product})


# -------------------- SERVICE --------------------
def service_list(request):
    services = Service.objects.all()
    return render(request, 'service/list.html', {'services': services})


def service_create(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Xizmat qo‘shildi ✅")
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'service/form.html', {'form': form})


def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, "Xizmat yangilandi ✏️")
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'service/form.html', {'form': form})


def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        service.delete()
        messages.success(request, "Xizmat o‘chirildi ❌")
        return redirect('service_list')
    return render(request, 'service/confirm_delete.html', {'object': service})


# -------------------- NEWS --------------------
def news_list(request):
    news_list = News.objects.all()
    return render(request, 'news/list.html', {'news_list': news_list})


def news_create(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Yangilik qo‘shildi ✅")
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news/form.html', {'form': form})


def news_edit(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            messages.success(request, "Yangilik yangilandi ✏️")
            return redirect('news_list')
    else:
        form = NewsForm(instance=news)
    return render(request, 'news/form.html', {'form': form})


def news_delete(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        news.delete()
        messages.success(request, "Yangilik o‘chirildi ❌")
        return redirect('news_list')
    return render(request, 'news/confirm_delete.html', {'object': news})


# -------------------- PARTNER --------------------
def partner_list(request):
    partners = Partner.objects.all()
    return render(request, 'partner/list.html', {'partners': partners})


def partner_create(request):
    if request.method == "POST":
        form = PartnerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Hamkor qo‘shildi ✅")
            return redirect('partner_list')
    else:
        form = PartnerForm()
    return render(request, 'partner/form.html', {'form': form})


def partner_edit(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == "POST":
        form = PartnerForm(request.POST, request.FILES, instance=partner)
        if form.is_valid():
            form.save()
            messages.success(request, "Hamkor yangilandi ✏️")
            return redirect('partner_list')
    else:
        form = PartnerForm(instance=partner)
    return render(request, 'partner/form.html', {'form': form})


def partner_delete(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == "POST":
        partner.delete()
        messages.success(request, "Hamkor o‘chirildi ❌")
        return redirect('partner_list')
    return render(request, 'partner/confirm_delete.html', {'object': partner})


# -------------------- GALLERY --------------------
def gallery_list(request):
    gallery = GalleryImage.objects.all()
    return render(request, 'gallery/list.html', {'gallery': gallery})


def gallery_create(request):
    if request.method == "POST":
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Rasm qo‘shildi ✅")
            return redirect('gallery_list')
    else:
        form = GalleryImageForm()
    return render(request, 'gallery/form.html', {'form': form})


def gallery_delete(request, pk):
    image = get_object_or_404(GalleryImage, pk=pk)
    if request.method == "POST":
        image.delete()
        messages.success(request, "Rasm o‘chirildi ❌")
        return redirect('gallery_list')
    return render(request, 'gallery/confirm_delete.html', {'object': image})


# -------------------- COMPANY INFO --------------------
def company_info_view(request):
    company = CompanyInfo.objects.first()
    if request.method == "POST":
        form = CompanyInfoForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, "Kompaniya ma'lumotlari yangilandi ✅")
            return redirect('company_info')
    else:
        form = CompanyInfoForm(instance=company)
    return render(request, 'company/form.html', {'form': form})
