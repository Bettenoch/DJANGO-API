from rest_framework import routers
from core.auth.viewsets.refresh import RefreshViewet
from core.auth.viewsets.register import RegisterViewSet, LoginViewSet
from core.user.viewsets import UserViewSet


router = routers.SimpleRouter()

router.register(r'users', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
routers.register(r'auth/refresh', RefreshViewet, basename='auth-refresh')
urlpatterns = [
    *router.urls
]