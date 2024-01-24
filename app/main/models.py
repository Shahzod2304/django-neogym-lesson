from django.db import models

# Create your models here.
class Home(models.Model):
    home_title = models.CharField(max_length=50)
    home_disc = models.TextField()

    def __str__(self):
        return self.home_title
    
    class Meta():
        verbose_name = "Home carusel"
        verbose_name_plural = "Home carusel"
    
class Why(models.Model):
    img = models.ImageField(upload_to='images/why')
    why_title = models.CharField(max_length=50)
    why_disc = models.TextField()

    def __str__(self):
        return self.why_title
    
    class Meta():
        verbose_name = "Why"
        verbose_name_plural = "Why"
    
class HomeContent(models.Model):
    home_content_title = models.CharField(max_length=50)
    home_content_disc = models.TextField()

    def __str__(self):
        return self.home_content_title
    
    class Meta():
        verbose_name = "Home content"
        verbose_name_plural = "Home content"

class Trainer(models.Model):
    full_name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/trainer')
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return self.full_name
    
    
class Footer(models.Model):
    location = models.URLField()
    phone_number = models.CharField(max_length=20)
    mail = models.CharField(max_length = 50)
    footer_text = models.CharField(max_length=100)

    def __str__(self):
        return "Нижняя часть сайта"
    
    class Meta():
        verbose_name = "Footer data"
        verbose_name_plural = "Footer data"