from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class News(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    excerpt = models.CharField(max_length=300, verbose_name="Qisqa mazmun")
    content = models.TextField(verbose_name="Mazmun")
    image = models.ImageField(upload_to='news/', verbose_name="Rasm")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Nashr sanasi")

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-published_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Partner(TimeStampedModel):
    logo = models.ImageField(upload_to='partners/', verbose_name="Logo")
    website = models.URLField(blank=True, verbose_name="Veb-sayt")

    class Meta:
        verbose_name = "Hamkor"
        verbose_name_plural = "Hamkorlar"

    def __str__(self):
        return self.logo


class GalleryImage(TimeStampedModel):
    image = models.ImageField(upload_to='gallery/', verbose_name="Rasm")

    class Meta:
        verbose_name = "Galereya rasmi"
        verbose_name_plural = "Galereya rasmlari"
        ordering = ['-created_at']

    def __str__(self):
        return self.image


class CompanyInfo(models.Model):
    company_name = models.CharField(max_length=200, verbose_name="Kompaniya nomi")
    about_us = models.TextField(verbose_name="Biz haqimizda")
    mission = models.TextField(verbose_name="Missiya")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    email = models.EmailField(verbose_name="Email")
    address = models.TextField(verbose_name="Manzil")
    facebook_url = models.URLField(blank=True, verbose_name="Facebook")
    instagram_url = models.URLField(blank=True, verbose_name="Instagram")
    telegram_url = models.URLField(blank=True, verbose_name="Telegram")
    youtube_url = models.URLField(blank=True, verbose_name="YouTube")
    image = models.ImageField(upload_to='company/', verbose_name='image')
    logo = models.ImageField(upload_to='company/', verbose_name="Logo")

    class Meta:
        verbose_name = "Kompaniya ma'lumotlari"
        verbose_name_plural = "Kompaniya ma'lumotlari"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and CompanyInfo.objects.exists():
            raise ValueError("Faqat bitta kompaniya ma'lumotlari yaratilishi mumkin")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.company_name
