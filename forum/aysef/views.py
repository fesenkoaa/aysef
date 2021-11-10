from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from .mixins import *
from datetime import datetime



class MainPage(View):

    def get(self, request):
        context = {
            'title': 'AYSEF'
        }
        return render(request, 'aysef/main.html', context)


class AboutPage(View):
    pass


class SendMessagePage(AddObjectMixin, View):

    model = Support
    template = 'aysef/message.html'
    form = MessageForm


class Forum(View):
    pass


class Themes(ListView):
    model = Category
    template_name = 'aysef/themes.html'
    paginate_by = 15
    extra_context = {
        'title': 'Themes',
    }


class TheTheme(View):
    pass


class AddTheme(View):
    pass


class DeleteTheme(View):
    pass


class TheArticle(View):
    pass


class AddArticle(View):
    pass


class EditArticle(View):
    pass


class DeleteArticle(View):
    pass


class Reg(View):
    pass


class Login(View):
    pass


class Logout(View):
    pass


class ResetPassword(View):
    pass


class ChangePassword(View):
    pass
