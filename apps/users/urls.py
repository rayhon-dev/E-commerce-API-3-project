from django.urls import path
from . import views


urlpatterns = [
    path('shop/profile/', views.UserProfileAPIView.as_view(), name='detail-update'),
]