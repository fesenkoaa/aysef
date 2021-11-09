from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import random


class Support(models.Model):

    number = models.DecimalField(max_digits=30, decimal_places=2, verbose_name='Number')
    message = models.CharField(max_length=255, verbose_name='Message')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Time')

    class Meta:
        ordering = '-time',

    def __repr__(self):
        return f'<{Support.__name__} ({self.number})>'

    def __str__(self):
        return self.number


class Category(models.Model):

    category = models.CharField(max_length=50, verbose_name='Theme')

    def __repr__(self):
        return f'<{Category.__name__} ({self.pk} {self.category})>'

    def __str__(self):
        return f'{self.pk} {self.category}'


class Article(models.Model):

    auth = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Auth')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='Theme')
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=9999)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'<{Article.__name__} ({self.auth}, {self.category}, {self.pk})>'

    def __str__(self):
        return f'{self.auth}, {self.category}, {self.pk}'

    def get_absolute_url(self):
        return reverse('forum', kwargs={'unique_pk': self.pk})