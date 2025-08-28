from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from medical.models.about import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class", verbose_name="Ikonka")

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    name = models.CharField(max_length=200, verbose_name="Mahsulot nomi")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")
    description = models.TextField(verbose_name="Tavsif")
    short_description = models.CharField(max_length=300, verbose_name="Qisqa tavsif")
    image = models.ImageField(upload_to='products/', verbose_name="Rasm")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Narx")
    composition = models.TextField(blank=True, verbose_name="Tarkib")
    dosage = models.CharField(max_length=100, blank=True, verbose_name="Dozasi")
    manufacturer = models.CharField(max_length=200, blank=True, verbose_name="Ishlab chiqaruvchi")

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Service(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name="Xizmat nomi")
    description = models.TextField(verbose_name="Tavsif")
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class", verbose_name="Ikonka")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Xizmat"
        verbose_name_plural = "Xizmatlar"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
