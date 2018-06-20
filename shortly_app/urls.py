from django.urls import path

from .views import DetailView, NewView, LinksView, TopView, ShortlyView

urlpatterns = [
    path('', TopView.as_view(), name='index'),
    path('list', LinksView.as_view(), name='list_short_url'),
    path('<int:shortly_id>/detail', DetailView.as_view(), name='detail'),
    path('<int:shortly_id>', ShortlyView.as_view(), name='follow_link'),
    path('new', NewView.as_view(), name='new'),
]