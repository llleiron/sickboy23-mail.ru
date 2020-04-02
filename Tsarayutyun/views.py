from rest_framework import generics
from .serializers import TsarayutyunCreateSerializer, TsarayutyunDetailSerializer, TsarayutyunListSerializer
from .models import Ծառայություն
# Create your views here.

class TsarayutyunCreateAPIView(generics.CreateAPIView):
    serializer_class = TsarayutyunCreateSerializer
    queryset = Ծառայություն.objects.all()

class TsarayutyunListAPIView(generics.ListAPIView):
    serializer_class = TsarayutyunListSerializer
    queryset = Ծառայություն.objects.all()

class TsarayutyunDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TsarayutyunDetailSerializer
    queryset = Ծառայություն.objects.all()
