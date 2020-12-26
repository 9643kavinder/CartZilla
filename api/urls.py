from django.urls import path, include
from rest_framework.authtoken import views
from . import views as api_views

urlpatterns = [
    path('', api_views.home, name='api-home'),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls'))
]