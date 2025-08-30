from django.shortcuts import render, get_object_or_404
from .models import *
from .models.mics import ManufacturingOverview, ProductionLine, Partner, PartnershipBenefit, GalleryCategory, Gallery, \
    News


def home_page(request):
    services = Service.objects.all()
    features = Feature.objects.all()
    contact = Contact.objects.first()
    internet = Internet.objects.all()

    ctx = {
        "services": services,
        "features": features,
        "contact": contact,
        'internet': internet
    }
    return render(request, "medical/index.html", ctx)


def about(request):
    mission = Mission.objects.first()
    points = MissionPoint.objects.all()
    stats = Statistic.objects.all()
    ctx = {
        "mission": mission,
        "points": points,
        "stats": stats,
        "values": Value.objects.all(),
        "achievements": Achievement.objects.all(),
        "members": Member.objects.all(),
        "histories": History.objects.all().order_by('year'),
        "contact": Contact.objects.first(),
        "internet": Internet.objects.all(),
    }
    return render(request, "medical/about.html", ctx)


def manufacturing_page(request):
    overview = ManufacturingOverview.objects.first()
    lines = ProductionLine.objects.all()
    return render(request, "medical/manufacturing.html", {
        "overview": overview,
        "lines": lines,
    })


def partners_page(request):
    partners = Partner.objects.all()
    benefits = PartnershipBenefit.objects.all()
    return render(request, "medical/partners.html", {
        "partners": partners,
        "benefits": benefits,
    })


def gallery_page(request):
    categories = GalleryCategory.objects.all()
    galleries = Gallery.objects.all()
    ctx = {
        "categories": categories,
        "galleries": galleries
    }

    return render(request, "medical/gallery.html", ctx)


def product_list(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    features = ProductFeature.objects.all()

    return render(request, "medical/products.html", {
        "categories": categories,
        "products": products,
        "features": features,
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:3]
    reviews = product.reviews.all()

    return render(request, "medical/product_detail.html", {
        "product": product,
        "related_products": related_products,
        "reviews": reviews,
    })


def news_list(request):
    news = News.objects.all().order_by("-date")
    return render(request, "medical/news.html", {"news_list": news})
