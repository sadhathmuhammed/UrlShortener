from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics, status
from rest_framework.response import Response
from .models import ShortURL
from .serializers import ShortURLSerializer
import string, random
from django.views import View 


class ShortenURLView(generics.CreateAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer

    def perform_create(self, serializer):
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        serializer.save(short_code=short_code)


class URLListView(generics.ListAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer


class RedirectURLView(View):
    def get(self, request, short_code):
        url_obj = get_object_or_404(ShortURL, short_code=short_code)
        return redirect(url_obj.original_url)
