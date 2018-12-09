from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('<str:pk>/', views.FilmDetailView.as_view(), name='film_detail'),

]