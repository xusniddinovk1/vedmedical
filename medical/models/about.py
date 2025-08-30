from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.sarlavha


class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.address


class Internet(models.Model):
    nomi = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return self.nomi


# Missiya (biz haqimizda)
class Mission(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField()
    image = models.ImageField(upload_to="missions/", blank=True, null=True)


    def __str__(self):
        return self.title


# Missiya punktlari (ikonka bilan)
class MissionPoint(models.Model):
    icon = models.CharField(max_length=50, default="fas fa-check-circle")
    title = models.CharField(max_length=255)
    context = models.TextField()

    def __str__(self):
        return self.title


# Statistikalar
class Statistic(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.number} {self.name}"


# Qadriyatlar
class Value(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    context = models.TextField()

    def __str__(self):
        return self.title


# Yutuqlar
class Achievement(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    context = models.TextField()
    year = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.title} ({self.year})"


# Jamoa
class Member(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to="team/")

    def __str__(self):
        return self.name


# Tarix (timeline)
class History(models.Model):
    year = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    context = models.TextField()

    def __str__(self):
        return f"{self.year} - {self.context}"
