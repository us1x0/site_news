from django.db import models
from django.forms import CharField


# Create your models here.
class News(models.Model):
    which_news = models.CharField(max_length=64)

    def __str__(self):
        return self.which_news


class OptionsNews(models.Model):
    news_zagalovok = models.CharField(max_length=128)
    news = models.CharField(max_length=1024)
    news_who_write = CharField(max_length=64)
    news_photo = models.ImageField(blank=True, null=True)
    news_date_time = models.CharField(max_length=32)
    news_category = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.news_zagalovok




