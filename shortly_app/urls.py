from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.catalog, name='list_short_url'),
    path('<int:shortly_id>/detail', views.detail, name='detail'),
    path('<int:shortly_id>', views.follow_link, name='follow_link'),
    path('new', views.new, name='new'),
]