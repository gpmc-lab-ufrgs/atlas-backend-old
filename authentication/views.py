from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
import json

from rest_framework.viewsets import ModelViewSet, ViewSet


from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

class LoginView(ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    @action(detail=False, methods=['post'])
    def login(self, request):
        request_body = json.loads(request.body)
        username = request_body.get('username')
        password = request_body.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user) #get the user's authentication token if it exists, or create a new one if it doesn't
                return Response({'msg': 'Successful', 'usr_pk': user.id, 'usr_token': str(token.key)})
            else:
                return Response({'msg': 'Not active'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'msg': 'Error'}, status=status.HTTP_401_UNAUTHORIZED)