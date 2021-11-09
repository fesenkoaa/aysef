from django.shortcuts import render
from django.views import View


class MainPage(View):

    def get(self, request):
        context = {
            'title': 'AYSEF'
        }
        return render(request, 'aysef/main.html', context)