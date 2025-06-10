from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from apps.users.infrastructure.repositories import DjangoUserRepository
from apps.users.application.use_cases import RegisterUser, LoginUser

class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        return render(request, "users/register.html")
    
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        username = request.data.get("username")
        
        try:
            repo = DjangoUserRepository()
            use_case = RegisterUser(repo)
            user = use_case.execute(email=email, password=password, username=username)
            
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        return render(request, "users/login.html")
    
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        repo = DjangoUserRepository()
        use_case = LoginUser(repo)
        result = use_case.execute(email=email, password=password)
        
        if result.success:
            token, created = Token.objects.get_or_create(user=result.user)
            
            return Response({
                "id": result.user.id, 
                "email": result.user.email,
                "username": result.user.username,
                "token": token.key
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": result.error
            }, status=status.HTTP_401_UNAUTHORIZED)