from django.urls import re_path

from rest_framework_simplejwt.views import TokenObtainPairView

from users.utils import MyTokenObtainPairView

from .views import statistics_views

app_name = 'admincenter'

urlpatterns = [
    # re_path(r'^authorizations/$', TokenObtainPairView.as_view(), name='admincenter_authorizations'),
    re_path(r'^authorizations/$', MyTokenObtainPairView.as_view(), name='admincenter_authorizations'),
    re_path(r'^statistical/total_count/$', statistics_views.UserTotalCountView.as_view(),
            name='admincenter_statistical_total_count'),
    re_path(r'^statistical/day_increment/$', statistics_views.UserDayCountView.as_view(),
            name='admincenter_statistical_day_increment'),
    re_path(r'^statistical/day_active/$', statistics_views.UserActiveCountView.as_view(),
            name='admincenter_statistical_day_active'),
    re_path(r'^statistical/day_orders/$', statistics_views.UserOrderCountView.as_view(),
            name='admincenter_statistical_day_orders'),
    re_path(r'^statistical/month_increment/$', statistics_views.UserMonthCountView.as_view(),
            name='admincenter_statistical_month_increment'),
    re_path(r'^statistical/goods_day_views/$', statistics_views.GoodsDayView.as_view(),
            name='admincenter_statistical_goods_day_views'),
]
