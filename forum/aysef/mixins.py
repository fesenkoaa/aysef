from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import EmailMessage
from datetime import datetime


class AddObjectMixin:

    model = None
    template = None
    form = None

    def get(self, request):
        form = self.form
        context = {
            'form': form,
        }

        return render(request, self.template, context)

    def post(self, request):
        form = self.form(request.POST)
        context = {'form': form}

        if form.is_valid():
            form.save()

        return redirect('forum')