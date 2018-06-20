from django.urls import path

from . import views
from .views import DetailView, NewView, LinksView

urlpatterns = [
    path('', views.index, name='index'),
    path('list', LinksView.as_view(), name='list_short_url'),
    # path('list', views.catalog, name='list_short_url'),
    # path('<int:shortly_id>/detail', views.detail, name='detail'),
    path('<int:shortly_id>/detail', DetailView.as_view(), name='detail'),
    path('<int:shortly_id>', views.follow_link, name='follow_link'),
    path('new', NewView.as_view(), name='new'),
    # path('new', views.new, name='new'),
]