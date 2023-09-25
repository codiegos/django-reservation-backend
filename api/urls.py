from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet, 'users')
router.register(r'cabins', views.CabinViewSet, 'cabins')
router.register(r'customers', views.CustomerViewSet, 'customers')
router.register(r'reservations', views.ReservationViewSet, 'reservations')
router.register(r'prepaids', views.PrepaidViewSet, 'prepaids')


urlpatterns = [
    path('', include(router.urls)),
]