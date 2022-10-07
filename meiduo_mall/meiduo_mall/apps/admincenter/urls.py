from django.urls import re_path

from rest_framework_simplejwt.views import TokenObtainPairView

from users.utils import MyTokenObtainPairView

from .views import statistics_view

app_name = 'admincenter'

urlpatterns = [
    # re_path(r'^authorizations/$', TokenObtainPairView.as_view(), name='admincenter_authorizations'),
    re_path(r'^authorizations/$', MyTokenObtainPairView.as_view(), name='admincenter_authorizations'),
    re_path(r'^statistical/total_count/$', statistics_view.UserTotalCountView.as_view(),
            name='admincenter_statistical_total_count'),
    re_path(r'^statistical/day_increment/$', statistics_view.UserDayCountView.as_view(),
            name='admincenter_statistical_day_increment'),
]
