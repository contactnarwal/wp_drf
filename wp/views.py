from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, UserDetailSerializer, UserUpdateSerializer, LoginSerializer

from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView,DestroyAPIView
from .models import User
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrOwner
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')  # Use `.get()` to avoid KeyError
            password = serializer.validated_data.get('password')

            user = authenticate(email=email, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({"message": "Login successful", "token": token.key}, status=status.HTTP_200_OK)
            
            return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # ✅ Fixed syntax

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'id'   
class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner]  # Only authenticated users can update their details
    lookup_field = 'id'  # Lookup user by ID  


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    lookup_field = "id"
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

