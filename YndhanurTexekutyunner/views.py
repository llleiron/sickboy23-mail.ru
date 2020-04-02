from rest_framework import generics
from YndhanurTexekutyunner.serializers import YndhanurTexekutyunnerCreateSerializer, YndhanurTexekutyunnerDetailSerializer, YndhanurTexekutyunnerListSerializer
from YndhanurTexekutyunner.models import ԸնդհանուրՏեղեկություններ

class YndhanurTexekutyunnerCreateAPIView(generics.CreateAPIView):
    serializer_class = YndhanurTexekutyunnerCreateSerializer
    queryset = ԸնդհանուրՏեղեկություններ.objects.all()

class YndhanurTexekutyunnerListAPIView(generics.ListAPIView):
    serializer_class = YndhanurTexekutyunnerListSerializer
    queryset = ԸնդհանուրՏեղեկություններ.objects.all()

class YndhanurTexekutyunnerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = YndhanurTexekutyunnerDetailSerializer
    queryset = ԸնդհանուրՏեղեկություններ.objects.all()
    