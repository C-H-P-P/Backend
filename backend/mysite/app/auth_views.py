from __future__ import annotations

from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from mysite.authentication import build_minimal_jwt


class MinimalLoginView(APIView):
    """Login that returns a *minimal* JWT (only userId + exp)."""

    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username") or request.data.get("login")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"detail": "username and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(request=request, username=username, password=password)
        if user is None:
            return Response(
                {"detail": "Invalid credentials"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        token = build_minimal_jwt(user)
        return Response({"access": token}, status=status.HTTP_200_OK)


class MinimalRegisterView(APIView):
    """Register that returns a *minimal* JWT (only userId + exp).

    Accepts either:
      - username, password
    or
      - username, password1, password2
    """

    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password") or request.data.get("password1")
        password2 = request.data.get("password2")

        if not username or not password:
            return Response(
                {"detail": "username and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if password2 is not None and password != password2:
            return Response(
                {"detail": "Passwords do not match"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        User = get_user_model()
        if User.objects.filter(username=username).exists():
            return Response(
                {"detail": "User already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.create_user(username=username, email=email, password=password)

        token = build_minimal_jwt(user)
        return Response({"access": token}, status=status.HTTP_201_CREATED)




class UserDetailView(APIView):
    """
    Повертає дані поточного авторизованого користувача.
    Вимагає заголовок: Authorization: Bearer <token>
    """
    permission_classes = [IsAuthenticated] # Тільки для тих, хто має токен

    def get(self, request):
        # request.user автоматично підставляється завдяки твоєму MinimalJWTAuthentication
        serializer = UserSerializer(request.user)
        return Response(serializer.data)