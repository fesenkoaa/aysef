from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import random


class EmailMessage(models.Model):

    email = models.EmailField(verbose_name='Email')
    message = models.CharField(max_length=255, verbose_name='Message')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Time')

    class Meta:
        ordering = '-time',

    def __repr__(self):
        return f'<{EmailMessage.__name__} ({self.email})>'

    def __str__(self):
        return f'{self.email}'


class Category(models.Model):

    category = models.CharField(max_length=50, verbose_name='Theme')

    def __repr__(self):
        return f'<{Category.__name__} ({self.pk} {self.category})>'

    def __str__(self):
        return f'{self.category}'


class Article(models.Model):

    auth = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Auth')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='Theme')
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=9999)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = '-created_at',

    def __repr__(self):
        return f'<{Article.__name__} ({self.auth}, {self.category}, {self.pk})>'

    def __str__(self):
        return f'{self.auth}, {self.category}, {self.pk}'

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})