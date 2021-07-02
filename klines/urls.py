from django.urls import path, include
from rest_framework import routers
from klines import views

router = routers.DefaultRouter()
router.register(r'klines', views.KlineView,
    basename='put-something-here')

urlpatterns = [
    path('', include(router.urls)),
]