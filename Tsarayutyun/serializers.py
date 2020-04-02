from rest_framework import serializers
from Tsarayutyun.models import Ծառայություն
from Grancum.models import Գրանցում



class TsarayutyunListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ծառայություն
        fields = '__all__'

class TsarayutyunDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ծառայություն
        fields = '__all__'

class TsarayutyunCreateSerializer(serializers.ModelSerializer):

    հհ_id = serializers.IntegerField()
    Ամսաթիվը = serializers.DateField()
    ԾառայութայնԵվԿենցաղայինՊայմանները = serializers.CharField()
    ԱշխատանքիԲնույթը = serializers.CharField()
    ԲնակկենցաղայինՊայմանները = serializers.CharField()
    Սնունդը = serializers.CharField()
    Քունը = serializers.CharField()
    ՖիզիկականՊատրաստությունը = serializers.CharField()
    Արձակուրդը = serializers.CharField()

    class Meta:
        model = Ծառայություն
        fields = (
            'հհ_id',
            'Ամսաթիվը',
            'ԾառայութայնԵվԿենցաղայինՊայմանները',
            'ԱշխատանքիԲնույթը',
            'ԲնակկենցաղայինՊայմանները',
            'Սնունդը',
            'Քունը',
            'ՖիզիկականՊատրաստությունը',
            'Արձակուրդը'
        )
        

    def create(self, validated_data):

        հհ_id = validated_data['հհ_id']
        Ամսաթիվը = validated_data['Ամսաթիվը']
        ԾառայութայնԵվԿենցաղայինՊայմանները = validated_data['ԾառայութայնԵվԿենցաղայինՊայմանները']
        ԱշխատանքիԲնույթը = validated_data['ԱշխատանքիԲնույթը']
        ԲնակկենցաղայինՊայմանները = validated_data['ԲնակկենցաղայինՊայմանները']
        Սնունդը = validated_data['Սնունդը']
        Քունը = validated_data['Քունը']
        ՖիզիկականՊատրաստությունը = validated_data['ՖիզիկականՊատրաստությունը']
        Արձակուրդը = validated_data['Արձակուրդը']

        try:
            հհ = Գրանցում.objects.get(pk=հհ_id)
        except Գրանցում.DoesNotExist:
            raise serializers.ValidationError('Այսպիսի հերթական համարով գրանցված զինծառայող գոյություն չունի, մուտքագրեք ճիշտ հ/հ')
        
        ծառայություն = Ծառայություն(
            հհ=հհ,
            Ամսաթիվը=Ամսաթիվը,
            ԾառայութայնԵվԿենցաղայինՊայմանները=ԾառայութայնԵվԿենցաղայինՊայմանները,
            ԱշխատանքիԲնույթը = ԱշխատանքիԲնույթը,
            ԲնակկենցաղայինՊայմանները = ԲնակկենցաղայինՊայմանները,
            Սնունդը = Սնունդը,
            Քունը = Քունը,
            ՖիզիկականՊատրաստությունը = ՖիզիկականՊատրաստությունը,
            Արձակուրդը = Արձակուրդը,
        )
        ծառայություն.save()
        return ծառայություն
