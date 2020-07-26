from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, status


class TokenError(Exception):
    pass


class TokenBackendError(Exception):
    pass


class DetailDictMixin:
    def __init__(self, detail=None, code=None):
        """
        Builds a detail dictionary for the error to give more information to API
        users.
        """
        detail_dict = {'key': self.default_code, 'message': self.default_detail}

        if isinstance(detail, dict):
            detail_dict.update(detail)
        elif detail is not None:
            detail_dict['message'] = detail

        if code is not None:
            detail_dict['key'] = code
        if code is None:
            detail_dict['key'] = 'authentification'

        super().__init__(detail_dict)


class AuthenticationFailed(DetailDictMixin, exceptions.AuthenticationFailed):
    pass


class InvalidToken(AuthenticationFailed):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('Token is invalid or expired')
    default_code = 'token_not_valid'
