import re

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# from .models import User

User = get_user_model()

# class UsernameMobileAuthBackend(ModelBackend):
#     def authenticate(self, request=None, username=None, password=None, **kwargs):
#         user = self.get_user_by_account(username)
#         if user and user.check_password(password):
#             return user
#
#     @staticmethod
#     def get_user_by_account(account):
#         regex = r'^1[3-9]\d{9}$'
#         if re.match(regex, account):
#             mobile = account
#             try:
#                 user = User.objects.get(mobile=mobile)
#             except User.DoesNotExist:
#                 return None
#             else:
#                 return user
#         else:
#             username = account
#             try:
#                 user = User.objects.get(username=username)
#             except User.DoesNotExist:
#                 return None
#             else:
#                 return user
class UsernameMobileAuthBackend(ModelBackend):
    def authenticate(self, request=None, username=None, password=None, **kwargs):
        print(request)
        print(type(request))
        print(dir(request))
        user = self.get_user_by_account(username)
        if user and user.check_password(password):
            return user

    @staticmethod
    def get_user_by_account(account):
        regex = r'^1[3-9]\d{9}$'
        if re.match(regex, account):
            mobile = account
            try:
                user = User.objects.get(mobile=mobile)
            except User.DoesNotExist:
                return None
            else:
                return user
        else:
            username = account
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
            else:
                return user


# def jwt_response_payload_handler(token, user=None, request=None):
#     """自定义jwt认证成功返回数据"""
#     data = {
#         'token': token,
#         'id': user.id,
#         'username': user.username
#     }
#     return data


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # token = super().get_token(user)
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    """
    {"typ":"JWT","alg":"HS256"}
    {"token_type":"access","exp":1665052993,"iat":1665052963,"jti":"6531ea46700e441a8e12a4614cbefe14","user_id":21,"username":"mduser"}
    """
    serializer_class = MyTokenObtainPairSerializer
