"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from product.views import *

router = SimpleRouter()
router.register('product', ProductViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)) # http://localhost:8000/api/v1/product/
    # path('api/v1/product/', ProductViewSet.as_view({'get': 'list'})),
    # path('api/v1/product/', ProductViewSet.as_view({'post': 'create'})),
    # path('api/v1/product/<int:pk>/', ProductViewSet.as_view({'put': 'update'}))
    # path('api/v1/product/', ProductAPIView.as_view()),
    # path('api/v1/create/', ProductCreateView.as_view()),
    # path('api/v1/product/<int:pk>/', ProductDeatilAPIView.as_view()),
    # path('api/v1/update/<int:pk>/', ProductUpdateView.as_view())
]
