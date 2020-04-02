from rest_framework import generics
from .serializers import MyusDetailSerializer, MyusListSerializer, MyusCreateSerializer
from .models import ՄյուսՄասնագետներ
# Create your views here.

class MyusCreateAPIView(generics.CreateAPIView):
    serializer_class = MyusCreateSerializer
    queryset = ՄյուսՄասնագետներ.objects.all()

class MyusListAPIView(generics.ListAPIView):
    serializer_class = MyusListSerializer
    queryset = ՄյուսՄասնագետներ.objects.all()

class MyusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MyusDetailSerializer
    queryset = ՄյուսՄասնագետներ.objects.all()
