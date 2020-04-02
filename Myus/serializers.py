from rest_framework import serializers
from Myus.models import ՄյուսՄասնագետներ
from Grancum.models import Գրանցում



class MyusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ՄյուսՄասնագետներ
        fields = '__all__'

class MyusDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ՄյուսՄասնագետներ
        fields = '__all__'

class MyusCreateSerializer(serializers.ModelSerializer):

    հհ_id = serializers.IntegerField()
    Ամսաթիվը = serializers.DateField()
    ՀետազոտմանՏվյալներ = serializers.CharField()

    class Meta:
        model = ՄյուսՄասնագետներ
        fields = (
            'հհ_id',
            'Ամսաթիվը',
            'ՀետազոտմանՏվյալներ'
        )
        

    def create(self, validated_data):

        հհ_id = validated_data['հհ_id']
        Ամսաթիվը = validated_data['Ամսաթիվը']
        ՀետազոտմանՏվյալներ = validated_data['ՀետազոտմանՏվյալներ']

        try:
            հհ = Գրանցում.objects.get(pk=հհ_id)
        except Գրանցում.DoesNotExist:
            raise serializers.ValidationError('Այսպիսի հերթական համարով գրանցված զինծառայող գոյություն չունի, մուտքագրեք ճիշտ հ/հ')
        
        մյուսՄասնագետներ = ՄյուսՄասնագետներ(
            հհ=հհ,
            Ամսաթիվը=Ամսաթիվը,
            ՀետազոտմանՏվյալներ=ՀետազոտմանՏվյալներ
        )

        մյուսՄասնագետներ.save()
        return մյուսՄասնագետներ
