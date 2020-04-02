from rest_framework import serializers
from Fizikakan.models import Ֆիզիկական
from Grancum.models import Գրանցում


class FizikakanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ֆիզիկական
        fields = '__all__'

class FizikakanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ֆիզիկական
        fields = '__all__'

class FizikakanCreateSerializer(serializers.ModelSerializer):

    հհ_id = serializers.IntegerField()
    Ամսաթիվը = serializers.DateField()
    Քաշը = serializers.IntegerField()
    Հասակը = serializers.IntegerField()
    ԿրծքավանդակիՇրջանագիծըՀանգիստ = serializers.IntegerField()
    ԿրծքավանդակիՇրջանագիծըՇնչելիս = serializers.IntegerField()
    ԿրծքավանդակիՇրջանագիծըԱրտաշնչելիս = serializers.IntegerField()
    ՓորիՇրջագիծը = serializers.IntegerField()
    Շնչաչափը = serializers.IntegerField()
    ՁեռքիՈՒժաչափըԱջ = serializers.IntegerField()
    ՁեռքիՈՒժաչափըՁախ = serializers.IntegerField()
    class Meta:
        model = Ֆիզիկական
        fields = (
            'հհ_id',
            'Ամսաթիվը',
            'Քաշը',
            'Հասակը',
            'ԿրծքավանդակիՇրջանագիծըՀանգիստ',
            'ԿրծքավանդակիՇրջանագիծըՇնչելիս',
            'ԿրծքավանդակիՇրջանագիծըԱրտաշնչելիս',
            'ՓորիՇրջագիծը',
            'Շնչաչափը',
            'ՁեռքիՈՒժաչափըԱջ',
            'ՁեռքիՈՒժաչափըՁախ',
        )
        

    def create(self, validated_data):

        հհ_id = validated_data['հհ_id']
        Ամսաթիվը = validated_data['Ամսաթիվը']
        Քաշը = validated_data['Քաշը']
        Հասակը = validated_data['Հասակը']
        ԿրծքավանդակիՇրջանագիծըՀանգիստ = validated_data['ԿրծքավանդակիՇրջանագիծըՀանգիստ']
        ԿրծքավանդակիՇրջանագիծըՇնչելիս = validated_data['ԿրծքավանդակիՇրջանագիծըՇնչելիս']
        ԿրծքավանդակիՇրջանագիծըԱրտաշնչելիս = validated_data['ԿրծքավանդակիՇրջանագիծըԱրտաշնչելիս']
        ՓորիՇրջագիծը = validated_data['ՓորիՇրջագիծը']
        Շնչաչափը = validated_data['Շնչաչափը']
        ՁեռքիՈՒժաչափըԱջ = validated_data['ՁեռքիՈՒժաչափըԱջ']
        ՁեռքիՈՒժաչափըՁախ = validated_data['ՁեռքիՈՒժաչափըՁախ']

        try:
            հհ = Գրանցում.objects.get(pk=հհ_id)
        except Գրանցում.DoesNotExist:
            raise serializers.ValidationError('Այսպիսի հերթական համարով գրանցված զինծառայող գոյություն չունի, մուտքագրեք ճիշտ հ/հ')
        
        ֆիզիկական = Ֆիզիկական(
            հհ=հհ,
            Ամսաթիվը=Ամսաթիվը,
            Քաշը=Քաշը,
            Հասակը = Հասակը,
            ԿրծքավանդակիՇրջանագիծըՀանգիստ = ԿրծքավանդակիՇրջանագիծըՀանգիստ,
            ԿրծքավանդակիՇրջանագիծըՇնչելիս = ԿրծքավանդակիՇրջանագիծըՇնչելիս,
            ԿրծքավանդակիՇրջանագիծըԱրտաշնչելիս = ԿրծքավանդակիՇրջանագիծըԱրտաշնչելիս,
            ՓորիՇրջագիծը = ՓորիՇրջագիծը,
            Շնչաչափը = Շնչաչափը,
            ՁեռքիՈՒժաչափըԱջ = ՁեռքիՈՒժաչափըԱջ,
            ՁեռքիՈՒժաչափըՁախ = ՁեռքիՈՒժաչափըՁախ
        )
        ֆիզիկական.save()
        return ֆիզիկական
