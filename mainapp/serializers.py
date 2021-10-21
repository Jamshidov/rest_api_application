from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class ClientsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['id', 'passport_series', 'firstname', 'lastname', 'phone']


class CarsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Cars
        fields = ['id', 'brand', 'model', 'rent_cost']


class ExtendOrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Extended_orders
        fields = ['id', 'order', 'extended_to']


class OrdersSerializers(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = ['id', 'client_id', 'cars', 'timestamp', 'from_date', 'to_date', 'extended_days', 'exday',
                  'days_count', 'extend_order_count']


class UsersSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class ClientFilterSerializers(serializers.ModelSerializer):

    class Meta:
        model = Clients
        fields = ['id', 'firstname', 'lastname', 'pay_sum']


class CarsFilterSerializers(serializers.ModelSerializer):

    class Meta:
        model = Cars
        fields = ['id', 'brand', 'model', 'rent_cost', 'car_count_in_order', 'total_profit']












