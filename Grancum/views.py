from rest_framework import generics
from Grancum.models import Գրանցում
from Grancum.serializers import(
    GrancumCreateSerializer,
    GrancumListSerializer,
    GrancumDetailSerializer
)
# Create your views here.

class GrancumCreateAPIView(generics.CreateAPIView):
    serializer_class = GrancumCreateSerializer
    queryset = Գրանցում.objects.all()

class GrancumListAPIView(generics.ListAPIView):
    serializer_class = GrancumListSerializer
    queryset = Գրանցում.objects.all()

class GrancumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GrancumDetailSerializer
    queryset = Գրանցում.objects.all()