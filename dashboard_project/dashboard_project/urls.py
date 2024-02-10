from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Add this
    path('', include('stocks_dashboard.urls')),  # We will create this next
]
