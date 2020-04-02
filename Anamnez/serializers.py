from rest_framework import serializers
from Anamnez.models import Անամնեզ
from Grancum.models import Գրանցում

class AnamnezListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Անամնեզ
        fields = '__all__'

class AnamnezDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Անամնեզ
        fields = '__all__'

class AnamnezCreateSerializer(serializers.ModelSerializer):

    հհ_id = serializers.IntegerField()
    ՀիվանդացելԷ = serializers.CharField()
    վիրավորումները = serializers.CharField()
    Կոնտուզիաները = serializers.CharField()
    Վիրահատությունները = serializers.CharField()
    ԱրձակուրդներըՀիվանդությանՊատճառով = serializers.CharField()
    ԲուժումնԱռողջարաններում = serializers.CharField()
    Ժառանգականությունը = serializers.CharField()
    ԻնչԴեղերՉիԿարողանումԸնդունել = serializers.CharField()
    ՆերարկումներիԱզդեցությունը = serializers.CharField()
    ՎնասակարՍովորությունները = serializers.CharField()
    ՀատուկՆշումներ = serializers.CharField()

    class Meta:
        model = Անամնեզ
        fields = (
            'հհ_id',
            'ՀիվանդացելԷ',
            'վիրավորումները',
            'Կոնտուզիաները',
            'Վիրահատությունները',
            'ԱրձակուրդներըՀիվանդությանՊատճառով',
            'ԲուժումնԱռողջարաններում',
            'Ժառանգականությունը',
            'ԻնչԴեղերՉիԿարողանումԸնդունել',
            'ՆերարկումներիԱզդեցությունը',
            'ՎնասակարՍովորությունները',
            'ՀատուկՆշումներ'
        )
        

    def create(self, validated_data):

        հհ_id = validated_data['հհ_id']
        ՀիվանդացելԷ = validated_data['ՀիվանդացելԷ']
        վիրավորումները = validated_data['վիրավորումները']
        Կոնտուզիաները = validated_data['Կոնտուզիաները']
        Վիրահատությունները = validated_data['Վիրահատությունները']
        ԱրձակուրդներըՀիվանդությանՊատճառով = validated_data['ԱրձակուրդներըՀիվանդությանՊատճառով']
        ԲուժումնԱռողջարաններում = validated_data['ԲուժումնԱռողջարաններում']
        Ժառանգականությունը = validated_data['Ժառանգականությունը']
        ԻնչԴեղերՉիԿարողանումԸնդունել = validated_data['ԻնչԴեղերՉիԿարողանումԸնդունել']
        ՆերարկումներիԱզդեցությունը = validated_data['ՆերարկումներիԱզդեցությունը']
        ՎնասակարՍովորությունները = validated_data['ՎնասակարՍովորությունները']
        ՀատուկՆշումներ = validated_data['ՀատուկՆշումներ']
        try:
            հհ = Գրանցում.objects.get(pk=հհ_id)
        except Գրանցում.DoesNotExist:
            raise serializers.ValidationError('Այսպիսի հերթական համարով գրանցված զինծառայող գոյություն չունի, մուտքագրեք ճիշտ հ/հ')
        
        անամնեզ = Անամնեզ(
            հհ=հհ,
            ՀիվանդացելԷ=ՀիվանդացելԷ,
            վիրավորումները=վիրավորումները,
            Կոնտուզիաները = Կոնտուզիաները,
            Վիրահատությունները = Վիրահատությունները,
            ԱրձակուրդներըՀիվանդությանՊատճառով = ԱրձակուրդներըՀիվանդությանՊատճառով,
            ԲուժումնԱռողջարաններում = ԲուժումնԱռողջարաններում,
            Ժառանգականությունը = Ժառանգականությունը,
            ԻնչԴեղերՉիԿարողանումԸնդունել = ԻնչԴեղերՉիԿարողանումԸնդունել,
            ՆերարկումներիԱզդեցությունը = ՆերարկումներիԱզդեցությունը,
            ՎնասակարՍովորությունները = ՎնասակարՍովորությունները,
            ՀատուկՆշումներ = ՀատուկՆշումներ
        )
        անամնեզ.save()
        return անամնեզ