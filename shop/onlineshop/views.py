from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def post_list(request):

    return HttpResponse('А вот и страничка с товарами...')
