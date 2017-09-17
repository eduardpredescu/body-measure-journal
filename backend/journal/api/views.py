from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from .permissions import UserPermission, IsOwner
from rest_framework_jwt.settings import api_settings
from . import serializers
from . import models

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class AuthRegister(generics.CreateAPIView):
    """
    Register a new user.
    """
    model = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        user = self.model.get(username=serializer.data['username'])
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response(
            {
            'token': token
            },
            status=status.HTTP_201_CREATED, headers=headers
        )


class UserList(generics.ListAPIView):
    permission_classes = (UserPermission,)
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer



class MeasurementList(generics.ListAPIView):
    permission_classes = (IsOwner,)
    queryset = models.Measurement.objects.all()
    serializer_class = serializers.MeasurementSerializer


class MeasurementDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwner,)
    serializer_class = serializers.MeasurementSerializer
    queryset = models.Measurement.objects.all()
