from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User  
from django.contrib.auth import get_user_model
#create operation on user module 
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name' ,'role']

    def create(self, validated_data):
        
        # Make sure you pass the necessary fields for your custom User model
        role = validated_data.pop('role', 'subscriber')
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role = role,
        )
        return user
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(required=True, write_only=True)

    # def validate(self, data):
    #     UserModel = get_user_model()
    #     user = UserModel.objects.filter(email=data['email']).first()
    #     if not user or not user.check_password(data['password']):
    #         raise serializers.ValidationError("Invalid email or password")
    #     return {"email": user.email, "message": "Login successful"}



    #Read operation on user module 
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'role']
        # update operation on user module 
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'role']  # Include fields that can be updated
        read_only_fields = ['email']  # Example: Email can't be updated
    def validate_role(self, value):
        if not self.context['request'].user.role == 'admin':
            raise serializers.ValidationError("You do not have permission to update roles.")
        return value

    def update(self, instance, validated_data):
        validated_data.pop('email', None)  # Ignore email if provided
        return super().update(instance, validated_data)