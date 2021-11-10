from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model
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

    def get(self, request):
        context = {
            'title': 'About AYSEF',
            'text': 'bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla-bla'
        }

        return render(request, 'aysef/about.html', context)


class SendMessagePage(AddObjectMixin, View):

    def get(self, request):
        form = MessageForm
        context = {
            'form': form,
        }

        return render(request, 'aysef/message.html', context)

    def post(self, request):
        form = MessageForm(request.POST)

        if form.is_valid():
            form.save()

            if form == MessageForm:

                number = Support.objects.get(number=form.cleaned_data['number'])
                message = Support.objects.get(message=form.cleaned_data['message'])
                message_text = f'{number} \n{message}'
                wa.sendwhatmsg("+48788608806", message_text, time_hour=int(datetime.now().strftime('%H')),
                               time_min=int(datetime.now().strftime('%M')) + 1)

            return redirect('main')

        return render(request, 'aysef/message.html', {'form': form})


class Forum(ListView):
    model = Article
    template_name = 'aysef/forum.html'
    paginate_by = 15
    extra_context = {
        'title': 'Forum',
    }

    def get_queryset(self):

        auth = self.request.GET.get('search')
        try:
            auth_id = User.objects.get(username=auth).id
        except:
            auth_id = None

        if auth_id:
            objects_list = Article.objects.filter(auth_id=auth_id)
        else:
            objects_list = Article.objects.all()

        return objects_list


class Themes(ListView):
    model = Category
    template_name = 'aysef/themes.html'
    paginate_by = 15
    extra_context = {
        'title': 'Themes',
    }


class TheTheme(View):

    def get(self, request, pk):
        obj = Article.objects.filter(category_id=pk)
        theme = Category.objects.get(id=pk)
        context = {
            'title': theme.category,
            'theme': theme,
            'obj': obj
        }

        return render(request, 'aysef/theme.html', context)


class MyArticles(View):

    def get(self, request, pk):
        obj = Article.objects.filter(auth_id=pk)
        user = User.objects.get(id=pk)
        context = {
            'obj': obj,
            'auth_id': pk,
            'username': user.username,
            'user': user
        }

        return render(request, 'aysef/my-article.html', context)


class TheArticle(View):

    def get(self, request, pk):
        obj = get_object_or_404(Article, pk=pk)
        context = {
            'title': obj.title,
            'content': obj.text,
            'auth': obj.auth,
            'theme': obj.category,
            'time': str(obj.created_at)[:16],
            'id': obj.id
        }

        return render(request, 'aysef/article.html', context)



class AddArticle(AddObjectMixin, View):
    model = Article
    template = 'aysef/add-article.html'
    form = AddArticleFrom


class EditArticle(View):
    def get(self, request, pk):
        obj = Article.objects.get(pk=pk)
        form = ArticleForm(instance=obj)
        context = {
            'title': 'edit()',
            'form': form,
            'object': obj
        }

        return render(request, 'aysef/edit-article.html', context)

    def post(self, request, pk):
        obj = Article.objects.get(pk=pk)
        form = ArticleForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            return redirect('forum')

        context = {
            'form': form,
            'object': obj
        }

        return render(request, 'aysef/edit-article.html', context)


class DeleteArticle(View):

    def get(self, request, pk):
        obj = Article.objects.get(pk=pk)

        return render(request, 'aysef/delete-article.html', {'obj': obj})

    def post(self, request, pk):
        obj = Article.objects.get(pk=pk)
        obj.delete()
        return redirect('forum')


class Reg(View):

    def get(self, request):
        form = RegForm()
        return render(request, 'aysef/reg.html', {'form': form})

    def post(self, request):
        form = RegForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                return redirect('login')
            except:
                form.add_error(None, 'Something is wrong! New user wasn\'t added.')

        else:
            return render(request, 'aysef/reg.html', {'form': form})


class Login(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'aysef/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.get_user()
            login(request, username)
            messages.success(request, f'welcome, {username}')
            return redirect('main')
        else:
            messages.error(request, 'something is wrong')
            return render(request, 'aysef/login.html', {'form': form})


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('login')


# class ResetPassword(View):
#     pass


class ChangePassword(View):

    def get(self, request):
        form = ChangePasswordForm(request.user)
        return render(request, 'aysef/change_pswrd.html', {'form': form})

    def post(self, request):
        form = ChangePasswordForm(request.user, data=request.POST)

        if form.is_valid():
            form.save()
            logout(request)
            messages.success(request, 'password was changed')
            return redirect('login')

        else:
            messages.error(request, 'something is wrong')
            return render(request, 'aysef/change_pswrd.html', {'form': form})
