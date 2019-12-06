from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClothesListView.as_view()),
]
