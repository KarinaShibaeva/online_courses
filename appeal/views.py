from django.http import HttpResponse
from django.shortcuts import render

from appeal.forms import AppealForm


def submit_appeal(request):
    if request.method == 'POST':
        form = AppealForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Заявка успешно отправлена!')
    else:
        form = AppealForm()
    return render(request, 'appeal/appeal.html', {'form':form})