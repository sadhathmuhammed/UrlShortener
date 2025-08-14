from django.urls import path
from .views import ShortenURLView, URLListView, RedirectURLView

urlpatterns = [
    path('api/shorten/', ShortenURLView.as_view(), name='shorten-url'),
    path('api/urls/', URLListView.as_view(), name='url-list'),
    path('<str:short_code>/', RedirectURLView.as_view(), name='redirect-url'),
]
