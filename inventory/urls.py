from django.urls import path, include
from rest_framework.routers import DefaultRouter
from knox import views as knox_views
from inventory.views.item import ItemViewSet
from inventory.views.supplier import SupplierViewSet
from inventory.views.supply import SupplyViewSet
from inventory.views.user import RegisterAPI, LoginApi

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'supplies', SupplyViewSet)

urlpatterns = [
    path('auth/register/', RegisterAPI.as_view(), name='register'),
    path('auth/login/', LoginApi.as_view(), name='login'),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('auth/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('', include(router.urls)),
]
