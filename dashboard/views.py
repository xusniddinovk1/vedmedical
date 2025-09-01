from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from medical.models import *
from .forms import *


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


def login_page(request):
    if request.method == "POST":
        phone = request.POST.get("phone_number")
        password = request.POST.get("password")

        user = authenticate(request, phone_number=phone, password=password)
        if user:
            login(request, user)
            return redirect('home_page')
        else:
            return render(request, "dashboard/login.html", {"error": "Incorrect credentials"})

    return render(request, "dashboard/login.html")


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')


@login_required_decorator
def my_profile(request):
    ctx = {
        'user': request.user,
    }
    return render(request, 'dashboard/profile/profile.html', ctx)


@login_required_decorator
def profile_edit(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('my_profile')
    else:
        form = ProfileForm(instance=user)

    ctx = {
        'form': form
    }

    return render(request, 'dashboard/profile/profile_edit.html', ctx)


@method_decorator(login_required, name='dispatch')
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'dashboard/profile/password_change.html'
    success_url = reverse_lazy('password_change_done')


@login_required_decorator
def home_page(request):
    products = Product.objects.all()
    news = News.objects.all()
    partners = Partner.objects.all()
    members = Member.objects.all()
    galleries = Gallery.objects.all()
    product_categories = ProductCategory.objects.all()
    statistics = Statistic.objects.all()
    achievements = Achievement.objects.all()

    items = [
        {
            "icon": "fa-users",
            "color": "#3b82f6",  # blue-500
            "count": products.count(),
            "label": "Mahsulotlar",
            "chart_data": [products.count(), products.count() // 2, products.count() // 3]
        },
        {
            "icon": "fa-book",
            "color": "#10b981",  # green-500
            "count": news.count(),
            "label": "Yangiliklar",
            "chart_data": [news.count(), news.count() // 2, news.count() // 3]
        },
        {
            "icon": "fa-bell",
            "color": "#ef4444",  # red-500
            "count": partners.count(),
            "label": "Hamkorlar",
            "chart_data": [partners.count(), partners.count() // 2, partners.count() // 3]
        },
        {
            "icon": "fa-star",
            "color": "#facc15",  # yellow-500
            "count": members.count(),
            "label": "Jamoa a'zolari",
            "chart_data": [members.count(), members.count() // 2, members.count() // 3]
        },
        {
            "icon": "fa-users",
            "color": "#3b82f6",  # blue-500
            "count": galleries.count(),
            "label": "Rasmlar",
            "chart_data": [galleries.count(), galleries.count() // 2, galleries.count() // 3]
        },
        {
            "icon": "fa-bell",
            "color": "#ef4444",  # red-500
            "count": product_categories.count(),
            "label": "Mahsulot kategoriyasi",
            "chart_data": [product_categories.count(), product_categories.count() // 2, product_categories.count() // 3]
        },
        {
            "icon": "fa-users",
            "color": "#3b82f6",  # blue-500
            "count": statistics.count(),
            "label": "Statistikalar",
            "chart_data": [statistics.count(), statistics.count() // 2, statistics.count() // 3]
        },
        {
            "icon": "fa-book",
            "color": "#10b981",  # green-500
            "count": achievements.count(),
            "label": "Yutuqlar",
            "chart_data": [achievements.count(), achievements.count() // 2, achievements.count() // 3]
        },
    ]
    return render(request, 'dashboard/index.html', {'items': items})


def service_list(request):
    services = Service.objects.all()
    return render(request, "dashboard/service/list.html", {"services": services})


def service_create(request):
    form = ServiceForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("service_list")
    return render(request, "dashboard/service/form.html", {"form": form})


def service_edit(request, id):
    service = get_object_or_404(Service, id=id)
    form = ServiceForm(request.POST or None, request.FILES or None, instance=service)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("service_list")
    return render(request, "dashboard/service/form.html", {"form": form, "service": service})


def service_delete(request, id):
    service = get_object_or_404(Service, id=id)
    service.delete()
    return redirect("service_list")


# ==============================
# FEATURE VIEWS
# ==============================
def feature_list(request):
    features = Feature.objects.all()
    return render(request, "dashboard/feature/list.html", {"features": features})


def feature_create(request):
    form = FeatureForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("feature_list")
    return render(request, "dashboard/feature/form.html", {"form": form})


def feature_edit(request, id):
    feature = get_object_or_404(Feature, id=id)
    form = FeatureForm(request.POST or None, request.FILES or None, instance=feature)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("feature_list")
    return render(request, "dashboard/feature/form.html", {"form": form, "feature": feature})


def feature_delete(request, id):
    feature = get_object_or_404(Feature, id=id)
    feature.delete()
    return redirect("feature_list")


# ==============================
# CONTACT VIEWS
# ==============================
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "dashboard/contact/list.html", {"contacts": contacts})


def contact_create(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("contact_list")
    return render(request, "dashboard/contact/form.html", {"form": form})


def contact_edit(request, id):
    contact = get_object_or_404(Contact, id=id)
    form = ContactForm(request.POST or None, instance=contact)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("contact_list")
    return render(request, "dashboard/contact/form.html", {"form": form, "contact": contact})


def contact_delete(request, id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    return redirect("contact_list")


# ==============================
# INTERNET VIEWS
# ==============================
def internet_list(request):
    items = Internet.objects.all()
    return render(request, "dashboard/internet/list.html", {"items": items})


def internet_create(request):
    form = InternetForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("internet_list")
    return render(request, "dashboard/internet/form.html", {"form": form})


def internet_edit(request, id):
    item = get_object_or_404(Internet, id=id)
    form = InternetForm(request.POST or None, instance=item)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("internet_list")
    return render(request, "dashboard/internet/form.html", {"form": form, "item": item})


def internet_delete(request, id):
    item = get_object_or_404(Internet, id=id)
    item.delete()
    return redirect("internet_list")


# ==============================
# MISSION VIEWS
# ==============================
def mission_list(request):
    missions = Mission.objects.all()
    return render(request, "dashboard/mission/list.html", {"missions": missions})


def mission_create(request):
    form = MissionForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("mission_list")
    return render(request, "dashboard/mission/form.html", {"form": form})


def mission_edit(request, id):
    mission = get_object_or_404(Mission, id=id)
    form = MissionForm(request.POST or None, request.FILES or None, instance=mission)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("mission_list")
    return render(request, "dashboard/mission/form.html", {"form": form, "mission": mission})


def mission_delete(request, id):
    mission = get_object_or_404(Mission, id=id)
    mission.delete()
    return redirect("mission_list")


# ==============================
# MISSION POINT VIEWS
# ==============================
def mission_point_list(request):
    points = MissionPoint.objects.all()
    return render(request, "dashboard/mission_point/list.html", {"points": points})


def mission_point_create(request):
    form = MissionPointForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("mission_point_list")
    return render(request, "dashboard/mission_point/form.html", {"form": form})


def mission_point_edit(request, id):
    point = get_object_or_404(MissionPoint, id=id)
    form = MissionPointForm(request.POST or None, instance=point)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("mission_point_list")
    return render(request, "dashboard/mission_point/form.html", {"form": form, "point": point})


def mission_point_delete(request, id):
    point = get_object_or_404(MissionPoint, id=id)
    point.delete()
    return redirect("mission_point_list")


# ==============================
# STATISTIC VIEWS
# ==============================
def statistic_list(request):
    stats = Statistic.objects.all()
    return render(request, "dashboard/statistic/list.html", {"stats": stats})


def statistic_create(request):
    form = StatisticForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("statistic_list")
    return render(request, "dashboard/statistic/form.html", {"form": form})


def statistic_edit(request, id):
    stat = get_object_or_404(Statistic, id=id)
    form = StatisticForm(request.POST or None, instance=stat)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("statistic_list")
    return render(request, "dashboard/statistic/form.html", {"form": form, "stat": stat})


def statistic_delete(request, id):
    stat = get_object_or_404(Statistic, id=id)
    stat.delete()
    return redirect("statistic_list")


# ==============================
# VALUE VIEWS
# ==============================
def value_list(request):
    values = Value.objects.all()
    return render(request, "dashboard/value/list.html", {"values": values})


def value_create(request):
    form = ValueForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("value_list")
    return render(request, "dashboard/value/form.html", {"form": form})


def value_edit(request, id):
    value = get_object_or_404(Value, id=id)
    form = ValueForm(request.POST or None, instance=value)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("value_list")
    return render(request, "dashboard/value/form.html", {"form": form, "value": value})


def value_delete(request, id):
    value = get_object_or_404(Value, id=id)
    value.delete()
    return redirect("value_list")


# ==============================
# ACHIEVEMENT VIEWS
# ==============================
def achievement_list(request):
    achievements = Achievement.objects.all()
    return render(request, "dashboard/achievement/list.html", {"achievements": achievements})


def achievement_create(request):
    form = AchievementForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("achievement_list")
    return render(request, "dashboard/achievement/form.html", {"form": form})


def achievement_edit(request, id):
    achievement = get_object_or_404(Achievement, id=id)
    form = AchievementForm(request.POST or None, instance=achievement)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("achievement_list")
    return render(request, "dashboard/achievement/form.html", {"form": form, "achievement": achievement})


def achievement_delete(request, id):
    achievement = get_object_or_404(Achievement, id=id)
    achievement.delete()
    return redirect("achievement_list")


# ==============================
# MEMBER VIEWS
# ==============================
def member_list(request):
    members = Member.objects.all()
    return render(request, "dashboard/member/list.html", {"members": members})


def member_create(request):
    form = MemberForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("member_list")
    return render(request, "dashboard/member/form.html", {"form": form})


def member_edit(request, id):
    member = get_object_or_404(Member, id=id)
    form = MemberForm(request.POST or None, request.FILES or None, instance=member)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("member_list")
    return render(request, "dashboard/member/form.html", {"form": form, "member": member})


def member_delete(request, id):
    member = get_object_or_404(Member, id=id)
    member.delete()
    return redirect("member_list")


# ==============================
# HISTORY VIEWS
# ==============================
def history_list(request):
    histories = History.objects.all()
    return render(request, "dashboard/history/list.html", {"histories": histories})


def history_create(request):
    form = HistoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("history_list")
    return render(request, "dashboard/history/form.html", {"form": form})


def history_edit(request, id):
    history = get_object_or_404(History, id=id)
    form = HistoryForm(request.POST or None, instance=history)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("history_list")
    return render(request, "dashboard/history/form.html", {"form": form, "history": history})


def history_delete(request, id):
    history = get_object_or_404(History, id=id)
    history.delete()
    return redirect("history_list")


# ---------------- MANUFACTURING OVERVIEW ----------------
def manufacturing_overview_list(request):
    items = ManufacturingOverview.objects.all()
    return render(request, 'dashboard/overview/list.html', {'items': items})


def manufacturing_overview_create(request):
    form = ManufacturingOverviewForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('overview_list')
    return render(request, 'dashboard/overview/form.html', {'form': form})


def manufacturing_overview_edit(request, id):
    obj = get_object_or_404(ManufacturingOverview, id=id)
    form = ManufacturingOverviewForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('overview_list')
    return render(request, 'dashboard/overview/form.html', {'form': form, 'object': obj})


def manufacturing_overview_delete(request, id):
    obj = get_object_or_404(ManufacturingOverview, id=id)
    obj.delete()
    return redirect('overview_list')


# ---------------- MANUFACTURING STAT ----------------
def manufacturing_stat_list(request):
    items = ManufacturingStat.objects.all()
    return render(request, 'dashboard/stat/list.html', {'items': items})


def manufacturing_stat_create(request):
    form = ManufacturingStatForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('stat_list')
    return render(request, 'dashboard/stat/form.html', {'form': form})


def manufacturing_stat_edit(request, id):
    obj = get_object_or_404(ManufacturingStat, id=id)
    form = ManufacturingStatForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('stat_list')
    return render(request, 'dashboard/stat/form.html', {'form': form, 'object': obj})


def manufacturing_stat_delete(request, id):
    obj = get_object_or_404(ManufacturingStat, id=id)
    obj.delete()
    return redirect('stat_list')


# ---------------- PRODUCTION LINE ----------------
def production_line_list(request):
    items = ProductionLine.objects.all()
    return render(request, 'dashboard/line/list.html', {'items': items})


def production_line_create(request):
    form = ProductionLineForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('line_list')
    return render(request, 'dashboard/line/form.html', {'form': form})


def production_line_edit(request, id):
    obj = get_object_or_404(ProductionLine, id=id)
    form = ProductionLineForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('line_list')
    return render(request, 'dashboard/line/form.html', {'form': form, 'object': obj})


def production_line_delete(request, id):
    obj = get_object_or_404(ProductionLine, id=id)
    obj.delete()
    return redirect('line_list')


# ---------------- PARTNER ----------------
def partner_list(request):
    items = Partner.objects.all()
    return render(request, 'dashboard/partner/list.html', {'items': items})


def partner_create(request):
    form = PartnerForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('partner_list')
    return render(request, 'dashboard/partner/form.html', {'form': form})


def partner_edit(request, id):
    obj = get_object_or_404(Partner, id=id)
    form = PartnerForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('partner_list')
    return render(request, 'dashboard/partner/form.html', {'form': form, 'object': obj})


def partner_delete(request, id):
    obj = get_object_or_404(Partner, id=id)
    obj.delete()
    return redirect('partner_list')


# ---------------- PARTNERSHIP BENEFIT ----------------
def partnership_benefit_list(request):
    items = PartnershipBenefit.objects.all()
    return render(request, 'dashboard/benefit/list.html', {'items': items})


def partnership_benefit_create(request):
    form = PartnershipBenefitForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('benefit_list')
    return render(request, 'dashboard/benefit/form.html', {'form': form})


def partnership_benefit_edit(request, id):
    obj = get_object_or_404(PartnershipBenefit, id=id)
    form = PartnershipBenefitForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('benefit_list')
    return render(request, 'dashboard/benefit/form.html', {'form': form, 'object': obj})


def partnership_benefit_delete(request, id):
    obj = get_object_or_404(PartnershipBenefit, id=id)
    obj.delete()
    return redirect('benefit_list')


# ---------------- GALLERY CATEGORY ----------------
def gallery_category_list(request):
    items = GalleryCategory.objects.all()
    return render(request, 'dashboard/gallery_category/list.html', {'items': items})


def gallery_category_create(request):
    form = GalleryCategoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('gallery_category_list')
    return render(request, 'dashboard/gallery_category/form.html', {'form': form})


def gallery_category_edit(request, id):
    obj = get_object_or_404(GalleryCategory, id=id)
    form = GalleryCategoryForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('gallery_category_list')
    return render(request, 'dashboard/gallery_category/form.html', {'form': form, 'object': obj})


def gallery_category_delete(request, id):
    obj = get_object_or_404(GalleryCategory, id=id)
    obj.delete()
    return redirect('gallery_category_list')


# ---------------- GALLERY ----------------
def gallery_list(request):
    items = Gallery.objects.all()
    return render(request, 'dashboard/gallery/list.html', {'items': items})


def gallery_create(request):
    form = GalleryForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('gallery_list')
    return render(request, 'dashboard/gallery/form.html', {'form': form})


def gallery_edit(request, id):
    obj = get_object_or_404(Gallery, id=id)
    form = GalleryForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('gallery_list')
    return render(request, 'dashboard/gallery/form.html', {'form': form, 'object': obj})


def gallery_delete(request, id):
    obj = get_object_or_404(Gallery, id=id)
    obj.delete()
    return redirect('gallery_list')


# ---------------- CATEGORY ----------------
def category_list(request):
    items = Category.objects.all()
    return render(request, 'dashboard/category/list.html', {'items': items})


def category_create(request):
    form = CategoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'dashboard/category/form.html', {'form': form})


def category_edit(request, id):
    obj = get_object_or_404(Category, id=id)
    form = CategoryForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'dashboard/category/form.html', {'form': form, 'object': obj})


def category_delete(request, id):
    obj = get_object_or_404(Category, id=id)
    obj.delete()
    return redirect('category_list')


# ---------------- NEWS ----------------
def news_list(request):
    items = News.objects.all()
    return render(request, 'dashboard/news/list.html', {'items': items})


def news_create(request):
    form = NewsForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('news_list')
    return render(request, 'dashboard/news/form.html', {'form': form})


def news_edit(request, id):
    obj = get_object_or_404(News, id=id)
    form = NewsForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('news_list')
    return render(request, 'dashboard/news/form.html', {'form': form, 'object': obj})


def news_delete(request, id):
    obj = get_object_or_404(News, id=id)
    obj.delete()
    return redirect('news_list')


def product_category_list(request):
    categories = ProductCategory.objects.all()
    return render(request, "dashboard/product_category/list.html", {"categories": categories})


def product_category_create(request):
    form = ProductCategoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("product_category_list")
    return render(request, "dashboard/category/form.html", {"form": form})


def product_category_edit(request, id):
    category = get_object_or_404(ProductCategory, id=id)
    form = ProductCategoryForm(request.POST or None, instance=category)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("product_category_list")
    return render(request, "dashboard/category/form.html", {"form": form, "category": category})


def product_category_delete(request, id):
    category = get_object_or_404(ProductCategory, id=id)
    category.delete()
    return redirect("product_category_list")


# ==============================
# PRODUCT CRUD
# ==============================
def product_list(request):
    products = Product.objects.all()
    return render(request, "dashboard/product/list.html", {"products": products})


def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("product_list")
    return render(request, "dashboard/product/form.html", {"form": form})


def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("product_list")
    return render(request, "dashboard/product/form.html", {"form": form, "product": product})


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect("product_list")


# ==============================
# PRODUCT FEATURE CRUD
# ==============================
def product_feature_list(request):
    features = ProductFeature.objects.all()
    return render(request, "dashboard/product_feature/list.html", {"features": features})


def product_feature_create(request):
    form = ProductFeatureForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("product_feature_list")
    return render(request, "dashboard/product_feature/form.html", {"form": form})


def product_feature_edit(request, id):
    feature = get_object_or_404(ProductFeature, id=id)
    form = ProductFeatureForm(request.POST or None, instance=feature)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("product_feature_list")
    return render(request, "dashboard/product_feature/form.html", {"form": form, "feature": feature})


def product_feature_delete(request, id):
    feature = get_object_or_404(ProductFeature, id=id)
    feature.delete()
    return redirect("product_feature_list")


# ==============================
# PRODUCT IMAGE CRUD
# ==============================
def image_list(request):
    images = ProductImage.objects.all()
    return render(request, "dashboard/image/list.html", {"images": images})


def image_create(request):
    form = ProductImageForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("image_list")
    return render(request, "dashboard/image/form.html", {"form": form})


def image_edit(request, id):
    image = get_object_or_404(ProductImage, id=id)
    form = ProductImageForm(request.POST or None, request.FILES or None, instance=image)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("image_list")
    return render(request, "dashboard/image/form.html", {"form": form, "image": image})


def image_delete(request, id):
    image = get_object_or_404(ProductImage, id=id)
    image.delete()
    return redirect("image_list")
