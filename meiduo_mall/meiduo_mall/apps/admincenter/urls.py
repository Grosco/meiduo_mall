from django.urls import re_path

from rest_framework_simplejwt.views import TokenObtainPairView

from users.utils import MyTokenObtainPairView

from . import views

app_name = 'admincenter'

urlpatterns = [
    # re_path(r'^authorizations/$', TokenObtainPairView.as_view(), name='admincenter_authorizations'),
    re_path(r'^authorizations/$', MyTokenObtainPairView.as_view(), name='admincenter_authorizations'),
    re_path(r'^statistical/total_count/$', views.UserTotalCountView.as_view(), name='admincenter_statistical_total_count'),
]
