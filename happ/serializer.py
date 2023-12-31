from rest_framework import serializers
from .models import *
class Productser(serializers.Serializer):
    no=serializers.IntegerField()
    name=serializers.CharField(max_length=30 )
    image=serializers.ImageField()
    price=serializers.IntegerField()
    details=serializers.CharField(max_length=50)


    def create(self, validated_data):
        return Addproduct.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.no=validated_data.get('no',instance.no)
        instance.name=validated_data.get('name',instance.no)
        instance.image=validated_data.get('image',instance.image)
        instance.price=validated_data.get('price',instance.price)
        instance.details=validated_data.get('details',instance.details)
        instance.save()
        return instance