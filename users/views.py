from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from .services import UserService
from .serializers import UserSerializer

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserService().get_users()

""" class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        service = UserService()
        return service.get_users()
    
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "id": user.id,
            "name": user.name,
            "email": user.email
        }, status=status.HTTP_201_CREATED) """
