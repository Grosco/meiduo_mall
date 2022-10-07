import re

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import update_last_login

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.settings import api_settings

# from .models import User

User = get_user_model()


class UsernameMobileAuthBackend(ModelBackend):
    def authenticate(self, request=None, username=None, password=None, **kwargs):
        #  as_admin为False的是Django调用的本方法
        as_admin = kwargs.get('as_admin', True)

        if as_admin:
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


# start # Customizing token claims #
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["token"] = data["access"]
        data["id"] = str(self.user.id)
        data["username"] = str(self.user.username)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    """
    自定义jwt认证成功返回数据
    {"typ":"JWT","alg":"HS256"}
    {"token_type":"access","exp":1665052993,"iat":1665052963,"jti":"6531ea46700e441a8e12a4614cbefe14","user_id":21,"username":"mduser"}
    """
    serializer_class = MyTokenObtainPairSerializer
# end # Customizing token claims #
