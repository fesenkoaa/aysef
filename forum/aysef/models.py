from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import random


class Theme(models.Model):

    theme = models.CharField(max_length=50, verbose_name='Theme'),
    theme_auth = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Auth'),

    class Meta:
        ordering = 'id',

    def __repr__(self):
        return f'<{Theme.__name__} ({self.theme[:10]} {self.theme_auth})>'

    def __str__(self):
        return self.theme

    def get_absolute_url(self):
        return reverse('forum/theme', kwargs={'unique_key': self.pk})


class Support(models.Model):

    number = models.DateTimeField(max_length=30)
    message = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = '-time',

    def __repr__(self):
        return f'<{Support.__name__} ({self.number})>'

    def __str__(self):
        return self.number


class Article(models.Model):

    auth = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Auth')
    theme = models.ForeignKey(Theme, on_delete=models.DO_NOTHING, verbose_name='Theme')
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=9999)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'<{Article.__name__} ({self.auth}, {self.theme}, {self.pk})>'

    def __str__(self):
        return f'{self.auth}, {self.theme}, {self.pk}'

    def get_absolute_url(self):
        return reverse('forum', kwargs={'unique_pk': self.pk})