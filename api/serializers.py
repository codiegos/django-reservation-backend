from rest_framework import serializers
from .validations import COLOR_VALIDATOR, PHONE_VALIDATOR
from .models import Cabin, Customer, Reservation, Prepaid, Setting, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class CabinSerializer(serializers.ModelSerializer):

    color = serializers.CharField(validators=[COLOR_VALIDATOR])
    price = serializers.IntegerField(min_value=0)

    class Meta:
        model = Cabin
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(validators=[PHONE_VALIDATOR])

    class Meta:
        model = Customer
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):

    amount = serializers.IntegerField(min_value=0)
    discount = serializers.IntegerField(min_value=0)

    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError(
                "La fecha inicial no puede ser mayor a la fecha final")

        overlapping_reservations = Reservation.objects.filter(
            cabin=data['cabin'],
            start_date__lt=data['end_date'],
            end_date__gt=data['start_date']
        )

        if overlapping_reservations.exists():
            raise serializers.ValidationError(
                "La cabaña ya se encuentra reservada en ese rango de fechas")

        return data


class PrepaidSerializer(serializers.ModelSerializer):

    amount = serializers.IntegerField(min_value=0)

    class Meta:
        model = Prepaid
        fields = '__all__'


class SettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Setting
        fields = '__all__'
