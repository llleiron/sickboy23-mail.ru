from rest_framework import serializers
from YndhanurTexekutyunner.models import ԸնդհանուրՏեղեկություններ
from Grancum.models import Գրանցում



class YndhanurTexekutyunnerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ԸնդհանուրՏեղեկություններ
        fields = '__all__'

class YndhanurTexekutyunnerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ԸնդհանուրՏեղեկություններ
        fields = '__all__'

class YndhanurTexekutyunnerCreateSerializer(serializers.ModelSerializer):

    հհ_id = serializers.IntegerField()
    Զինկոչումը = serializers.CharField()
    ԱրյանԽումբը = serializers.CharField()
    ԾննդյանՏարեթիվը = serializers.CharField()
    Ազգությունը = serializers.CharField()
    Կրթությունը = serializers.CharField()
    ԾառայությանԱնցնելուԱմսաթիվը = serializers.DateField()
    ԸնտանեկանԴրությունը = serializers.CharField()
    ՏանՀասցեն = serializers.CharField()
    ՏանՀեռախոսահամարը = serializers.IntegerField()
    ԾառայավայրիՀասցեն = serializers.CharField(max_length = 1000)
    ԾառայավայրիՀեռախոսահամարը = serializers.IntegerField()
    class Meta:
        model = ԸնդհանուրՏեղեկություններ
        fields = (
            'հհ_id',
            'Զինկոչումը',
            'ԱրյանԽումբը',
            'ԾննդյանՏարեթիվը',
            'Ազգությունը',
            'Կրթությունը',
            'ԾառայությանԱնցնելուԱմսաթիվը',
            'ԸնտանեկանԴրությունը',
            'ՏանՀասցեն',
            'ՏանՀեռախոսահամարը',
            'ԾառայավայրիՀասցեն',
            'ԾառայավայրիՀեռախոսահամարը'
        )
        

    def create(self, validated_data):

        հհ_id = validated_data['հհ_id']
        Զինկոչումը = validated_data['Զինկոչումը']
        ԱրյանԽումբը = validated_data['ԱրյանԽումբը']
        ԾննդյանՏարեթիվը = validated_data['ԾննդյանՏարեթիվը']
        Ազգությունը = validated_data['Ազգությունը']
        Կրթությունը = validated_data['Կրթությունը']
        ԾառայությանԱնցնելուԱմսաթիվը = validated_data['ԾառայությանԱնցնելուԱմսաթիվը']
        ԸնտանեկանԴրությունը = validated_data['ԸնտանեկանԴրությունը']
        ՏանՀասցեն = validated_data['ՏանՀասցեն']
        ՏանՀեռախոսահամարը = validated_data['ՏանՀեռախոսահամարը']
        ԾառայավայրիՀասցեն = validated_data['ԾառայավայրիՀասցեն']
        ԾառայավայրիՀեռախոսահամարը = validated_data['ԾառայավայրիՀեռախոսահամարը']
        try:
            հհ = Գրանցում.objects.get(pk=հհ_id)
        except Գրանցում.DoesNotExist:
            raise serializers.ValidationError('Այսպիսի հերթական համարով գրանցված զինծառայող գոյություն չունի, մուտքագրեք ճիշտ հ/հ')
        
        ընդհանուրՏեղեկություններ = ԸնդհանուրՏեղեկություններ(
            հհ=հհ,
            Զինկոչումը=Զինկոչումը,
            ԱրյանԽումբը=ԱրյանԽումբը,
            ԾննդյանՏարեթիվը = ԾննդյանՏարեթիվը,
            Ազգությունը = Ազգությունը,
            Կրթությունը = Կրթությունը,
            ԾառայությանԱնցնելուԱմսաթիվը = ԾառայությանԱնցնելուԱմսաթիվը,
            ԸնտանեկանԴրությունը = ԸնտանեկանԴրությունը,
            ՏանՀասցեն = ՏանՀասցեն,
            ՏանՀեռախոսահամարը = ՏանՀեռախոսահամարը,
            ԾառայավայրիՀասցեն = ԾառայավայրիՀասցեն,
            ԾառայավայրիՀեռախոսահամարը = ԾառայավայրիՀեռախոսահամարը
        )
        ընդհանուրՏեղեկություններ.save()
        return ընդհանուրՏեղեկություններ
