from rest_framework import serializers
from .models import User
from rest_framework.exceptions import NotFound,ValidationError,AuthenticationFailed

# User Serializerx=1
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model=User
        fields= '__all__' #('username', 'email', 'mobile_no', 'gender', 'year', 'password')
        extra_kwargs = {'password': {'write_only': True,'required': False}}
    
   
    def create(self, validated_data): 
        return User.objects.create_user(**validated_data)

    def get(self, pk):

        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound("User Not Found")

    def update(self, instance, validated_data):
        
        instance.username = validated_data.get('username',instance.username)
        instance.mobile_no = validated_data.get('mobile_no',instance.mobile_no)
        instance.gender = validated_data.get('gender',instance.gender)
        instance.year = validated_data.get('year',instance.year)  
        instance.about = validated_data.get('about',instance.about)
        instance.profile_pic = validated_data.get('profile_pic',instance.profile_pic)
        instance.address = validated_data.get('address',instance.address)
 
        return instance

    def remove(self,pk):

        return User.objects.get(pk=pk).delete()

    def get_all(self):
        return User.objects.all()
