import re

from rest_framework.exceptions import NotAuthenticated
from rest_framework.exceptions import ValidationError

from .models import User

class AuthRequestManager():

    # validate
    # authenticate
    # exception handling

    def __init__(self, request):
        self.__request = request

    def __is_authorization_exists(self):
        return "Authorization" in self.__request.headers
    
    def __is_user(self, email=None):
        try:
            User.objects.get(pk=email)
            return True
        except:
            return False

    def is_invalid_email(self, email=None):
        
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        return re.search(regex, email) is None

    def is_invalid_password_pattern(self, password=None):

        pattern = re.compile('^(?=\S{8,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')
        return re.search(pattern, password) is None

    def is_valid_credentials(self, email=None, password=None):

        if self.is_invalid_email(email):
            raise ValidationError("Email Address Credentials Not Matched")

        if self.is_invalid_password_pattern(password):
            raise ValidationError("Password Credentials Not Matched")

        return True

    def is_valid(self):

        if not self.__is_authorization_exists():
            raise NotAuthenticated("Authorization Required")

        if not self.__is_valid_token():
            raise ValidationError("Invalid Token Error")

        return True