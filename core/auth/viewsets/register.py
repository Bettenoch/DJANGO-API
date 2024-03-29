from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from core.auth.serializers import RegisterSerializer

class RegisterViewSet(ViewSet):
    serialer_class = RegisterSerializer
    permission_classes = (AllowAny)
    http_method_names = ['POST']
    def create(self, request, *args, **kwargs):
        serializer = self.serialer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response({
            'user': serializer.data,
            'refresh':res['refresh'],
            'token': res['access']
            
        }, status=status.HTTP_201_created)
        