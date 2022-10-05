from django.urls import re_path
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views

app_name = 'admincenter'

urlpatterns = [
    re_path(r'^authorizations/$', TokenObtainPairView.as_view(), name='admincenter_authorizations'),
]
