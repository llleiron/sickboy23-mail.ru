from rest_framework import serializers
from Grancum.models import Գրանցում

class GrancumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Գրանցում
        fields = '__all__'

class GrancumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Գրանցում
        fields = '__all__'

class GrancumDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Գրանցում
        fields = '__all__'