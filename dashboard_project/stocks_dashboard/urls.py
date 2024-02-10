from django.urls import path
from .views import dashboard, stock_detail

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('stock/<str:symbol>/', stock_detail, name='stock_detail'),

]
