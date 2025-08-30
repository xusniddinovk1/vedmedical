from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="products")
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="products/")  # asosiy rasm
    badge = models.CharField(max_length=50, blank=True, null=True)  # "Yangi", "Mashhur"
    specs = models.JSONField(default=dict, blank=True)  # {"hajm": "1ml", "harorat": "2-8°C"}
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    certificates = models.CharField(max_length=255, blank=True, null=True)
    stock_status = models.BooleanField(default=True)
    rating = models.FloatField(default=0)
    reviews_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class ProductFeature(models.Model):
    icon = models.CharField(max_length=50, default="fas fa-check-circle")
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "Mahsulot afzalligi"
        verbose_name_plural = "Mahsulot afzalliklari"

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/gallery/")

    def __str__(self):
        return f"{self.product.title} rasmi"


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    reviewer = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(default=5)
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer} → {self.product.title}"
