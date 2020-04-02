from rest_framework import generics
from .serializers import AnamnezCreateSerializer, AnamnezListSerializer, AnamnezDetailSerializer
from .models import Անամնեզ

class AnamnezCreateAPIView(generics.CreateAPIView):
    serializer_class = AnamnezCreateSerializer
    queryset = Անամնեզ.objects.all()

class AnamnezListAPIView(generics.ListAPIView):
    serializer_class = AnamnezListSerializer
    queryset = Անամնեզ.objects.all()

class AnamnezDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnamnezDetailSerializer
    queryset = Անամնեզ.objects.all()

