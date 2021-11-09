from django.shortcuts import render
from django.views import View


class MainPage(View):

    def get(self, request):
        context = {
            'title': 'AYSEF'
        }
        return render(request, 'aysef/main.html', context)


class AboutPage(View):
    pass


class SendMessagePage(View):
    pass


class Forum(View):
    pass


class Themes(View):
    pass


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