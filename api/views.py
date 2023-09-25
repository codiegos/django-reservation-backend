from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .models import Cabin, Customer, Reservation, Prepaid, User, Setting
from .serializers import CabinSerializer, CustomerSerializer, ReservationSerializer, PrepaidSerializer, CustomTokenObtainPairSerializer, UserSerializer, SettingSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CabinViewSet(viewsets.ModelViewSet):
    serializer_class = CabinSerializer
    queryset = Cabin.objects.all()


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()


class PrepaidViewSet(viewsets.ModelViewSet):
    serializer_class = PrepaidSerializer
    queryset = Prepaid.objects.all()


class SettingViewSet(viewsets.ModelViewSet):
    serializer_class = SettingSerializer
    queryset = Setting.objects.all()


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = UserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh_token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Ha iniciado sesión correctamente'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first()).blacklist()
            return Response({'success': 'Ha cerrado sesión correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'Usuario inválido'}, status=status.HTTP_400_BAD_REQUEST)


class Register(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'success': 'El usuario se ha registrado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
