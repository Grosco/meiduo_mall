import re

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# from .models import User

User = get_user_model()


class UsernameMobileAuthBackend(ModelBackend):
    def authenticate(self, request=None, username=None, password=None, **kwargs):
        #  is_admin为False的是Django调用的本方法
        is_admin = kwargs.get('is_admin', True)

        if is_admin:
            user = self.get_user_by_account(account=username, is_staff=True)
        else:
            user = self.get_user_by_account(account=username, is_staff=False)

        if user and user.check_password(password):
            return user

    @staticmethod
    def get_user_by_account(account, is_staff):
        regex = r'^1[3-9]\d{9}$'
        if re.match(regex, account):
            mobile = account
            try:
                if is_staff:
                    user = User.objects.get(mobile=mobile, is_staff=True)
                else:
                    user = User.objects.get(mobile=mobile)
            except User.DoesNotExist:
                return None
            else:
                return user
        else:
            username = account
            try:
                if is_staff:
                    user = User.objects.get(username=username, is_staff=True)
                else:
                    user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
            else:
                return user


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
