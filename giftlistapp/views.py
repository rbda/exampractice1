from django.shortcuts import render
from django.views.generic import ListView

from giftlistapp.models import Clothes


class ClothesListView(ListView):

    model = Clothes
    # template_name = "something_else.html"

