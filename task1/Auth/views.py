from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.response import Response

from .auth_manager import AuthRequestManager
from .serializers import UserSerializer
from .models import User

from django.http import HttpResponse

from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.tokens import RefreshToken

class Auth(APIView):
    
    @api_view(['POST'])
    @permission_classes([AllowAny])
    def register(self):
        auth_request_manager = AuthRequestManager(self)
        if not auth_request_manager.is_invalid_email(email=self.data['email']) :
            if(User.objects.filter(email=self.data['email']).exists()):
                return Response(data={"status":400, "error":"Bad Request", "message":"User already exist"})
            else:
                try:
                    user = UserSerializer.create(self,validated_data=self.data.copy())
                    return Response(data={"message":"user created"},status=status.HTTP_200_OK)
                except KeyError:
                    return Response(data={"status":400, "error":"Bad Request", "message":"Required Parameters Missing"},status=status.HTTP_400_BAD_REQUEST)
        else:
            raise ValidationError("Email Address Credentials Not Matched")
    
    @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def get(self):
        token = self.headers['Authorization'].split(' ')[1]
        try:
            valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
            user_id = valid_data['user_id']
            user = User.objects.get(id=user_id)
            serializers = UserSerializer(user)
            return Response(serializers.data)
        except ValidationError as v:
            return ("validation error", v)
    
    @api_view(['PATCH'])
    @permission_classes([IsAuthenticated])
    def update(self):
        token = self.headers['Authorization'].split(' ')[1]
        try:
            valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
            user_id = valid_data['user_id']
            user = User.objects.get(id=user_id)
            updated_user = UserSerializer.update(self,instance=user,validated_data=self.data)
            serializer = UserSerializer(updated_user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except ValidationError as v:
            return ("validation error", v)

    @api_view(['DELETE'])
    @permission_classes([IsAuthenticated])
    def delete(self):
        token = self.headers['Authorization'].split(' ')[1]
        try:
            valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
            user_id = valid_data['user_id']
            user = User.objects.get(id=user_id)
            user.delete()
            return Response({"status":status.HTTP_200_OK,"message":"User Deleted"})
        except ValidationError as v:
            return ("validation error", v)
    
    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def logout(self):
        token = self.headers['Authorization'].split(' ')[1]
        try:
            valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
            user_id = valid_data['user_id']
            user = User.objects.get(id=user_id)
            token = RefreshToken.for_user(user)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

def page(request):
    return HttpResponse('For user registration needed fields are email,username,mobile_no at /auth/register/')

