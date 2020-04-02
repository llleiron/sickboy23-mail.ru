from rest_framework import generics
from .models import Ֆիզիկական
from .serializers import FizikakanCreateSerializer, FizikakanDetailSerializer, FizikakanListSerializer
# Create your views here.

class FizikakanCreateAPIView(generics.CreateAPIView):
    serializer_class = FizikakanCreateSerializer
    queryset = Ֆիզիկական.objects.all()

class FizikakanListAPIView(generics.ListAPIView):
    serializer_class = FizikakanListSerializer
    queryset = Ֆիզիկական.objects.all()

class FizikakanDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FizikakanDetailSerializer
    queryset = Ֆիզիկական.objects.all()
