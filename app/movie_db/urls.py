from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('new/', views.TitleCreateView.as_view(), name='title_new'),
    path('<str:pk>/', views.FilmDetailView.as_view(), name='film_detail'),
    path('<str:pk>/update/', views.TitleUpdateView.as_view(), name='title_update'),
    # path('<str:pk>/delete/', views.TitleDeleteView.as_view(), name='title_delete')


]