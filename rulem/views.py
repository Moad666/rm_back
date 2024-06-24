from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Rules
from .serializers import UserSerializer, RulesSerializer
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import generics, permissions



# User Register
class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# User Authentication
class Login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        # exp : sets the expiration time claim for the JWT
        # iat : specifies the time at which the token was issued
        payload= {
            'id' : user.id,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.utcnow()
        }

        # encodes the payload into a JSON Web Token (JWT) using the PyJWT
        # secret : secret key for encoding the token
        # The hashing algorithm used to generate the signature for the token
        # decode : used to convert token to a string
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        
        # create a response object
        response = Response()
        # set the token in cookies
        response.set_cookie(key='token', value=token, httponly=True)
        # return the token in the response body as well
        response.data = {'token': token}
        
        return response

# get all Users
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

# Delete User
class UserDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

# Create Rule
class RuleCreateAPIView(generics.ListCreateAPIView):
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer
    permission_classes = []

# List Rules
class RuleListAPIView(generics.ListAPIView):
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer
    permission_classes = []

# Update Rules
class RuleUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer
    permission_classes = []

# Delete Rule
class RuleDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer
    permission_classes = []

