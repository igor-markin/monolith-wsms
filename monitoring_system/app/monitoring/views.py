# from django.shortcuts import render
from django.http import HttpResponse

from .tasks import test_task

def test_view(request):
    answer = test_task.delay()
    return HttpResponse(answer)
