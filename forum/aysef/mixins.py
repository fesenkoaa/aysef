from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Support
from datetime import datetime
import pywhatkit as wa


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

            # if form == MessageForm:
            #
            #     number = Support.objects.get(number=form.cleaned_data['number'])
            #     message = Support.objects.get(message=form.cleaned_data['message'])
            #     message_for_send = f'{number} \n{message}'
            #     wa.sendwhatmsg("+48788608806", message_for_send, time_hour=int(datetime.now().strftime('%H')),
            #                    time_min=int(datetime.now().strftime('%M')))
            #
            # return redirect('main')

        return redirect('forum')