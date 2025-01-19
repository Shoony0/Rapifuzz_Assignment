from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import ForgotPasswordSerializer, GetIncidentSerializer, RegisterIncidentSerializer, RegisterSerializer, UpdateIncidentStatusSerializer, UserSerializer, ViewIncidentSerializer
from accounts.models import Incident, User
import requests

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

class LoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"user_id": user.id, "token": token.key})
        return Response({"error": "Invalid Credentials"}, status=400)

class ForgotPasswordView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ForgotPasswordSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        user = self.request.user   # get the authenticated user
        return User.objects.filter(id=user.id)  # filter by the current user
    
    
class RegisterIncidentView(generics.CreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = RegisterIncidentSerializer
    permission_classes = (IsAuthenticated,)
    
class IncidentView(generics.ListAPIView):
    queryset = Incident.objects.all()
    serializer_class = ViewIncidentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user   # get the authenticated user
        return Incident.objects.filter(user=user)  # filter by the current user
    
class GetIncidentView(generics.RetrieveAPIView):
    queryset = Incident.objects.all()
    serializer_class = GetIncidentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user   # get the authenticated user
        return Incident.objects.filter(user=user)  # filter by the current user
    
class UpdateIncidentStatusView(generics.UpdateAPIView):
    queryset = Incident.objects.all()
    serializer_class = UpdateIncidentStatusSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        user = self.request.user   # get the authenticated user
        return Incident.objects.filter(user=user)  # filter by the current user
    
class PincodeDetailsView(APIView):

    def get(self, request, pincode):
        data = requests.get(f"https://api.zippopotam.us/in/{pincode}")

        return Response(data.json(), status=200)