from django.contrib.auth import get_user_model
from datetime import datetime
from rest_framework_jwt.settings import api_settings



def jwt_payload_handler(user):
    email_field = username_field = get_user_model().USERNAME_FIELD
    email = user.get_username()

    payload = {
        'user_id': user.pk,
        'email': email,
        'username': user.username,
        'is_admin': user.is_admin,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }

    payload[username_field] = email

    # Include original issued at time for a brand new token,
    # to allow token refresh
    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(
            datetime.utcnow().utctimetuple()
        )

    if api_settings.JWT_AUDIENCE is not None:
        payload['aud'] = api_settings.JWT_AUDIENCE

    if api_settings.JWT_ISSUER is not None:
        payload['iss'] = api_settings.JWT_ISSUER

    return payload