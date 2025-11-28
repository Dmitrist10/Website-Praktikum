from django.urls import path, include
from .views import SubscribeEnginePremium

app_name = 'accounts'

urlpatterns = [
    path('', include('allauth.urls')),
    path('subscribe/engine/premium', SubscribeEnginePremium.as_view(), name='subscribe_engine_premium'),
]
