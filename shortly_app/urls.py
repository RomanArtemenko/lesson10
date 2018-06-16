from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.catalog, name='list_short_url'),
    path('<int:shortly_id>', views.detail, name='detail'),
    path('new', views.new, name='new'),
]