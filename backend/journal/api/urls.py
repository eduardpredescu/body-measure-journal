from django.conf.urls import include, url
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    url(r'^login/', obtain_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^register/', views.AuthRegister.as_view()),
    url(r'^measurements/$', views.MeasurementList.as_view()),
    url(r'^measurements/(?P<pk>[0-9]+)/$', views.MeasurementDetail.as_view()),
    ]