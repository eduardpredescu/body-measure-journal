from django.conf.urls import include, url
from django.contrib.auth.views import logout
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    url(r'^login/', obtain_jwt_token),
    url(r'^logout/', logout),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^register/$', views.AuthRegister.as_view()),
]