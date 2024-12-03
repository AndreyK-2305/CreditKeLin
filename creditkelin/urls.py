from django.contrib import admin
from django.urls import path, include
from credit.views import CreditViewSet, PaymentViewSet
from products.views import ProductTypeViewSet, ProductViewSet
from users.views import UserViewSet, LoginView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'credits', CreditViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'product-type', ProductTypeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('credits/<int:pk>/payments/', CreditViewSet.as_view({'get': 'payments'}), name='credit-payments'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('clients/<int:pk>/credits/', UserViewSet.as_view({'get': 'credits'}), name='client-credits'), 
]
