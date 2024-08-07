import jwt
import requests
from time import sleep
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login,logout
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.permissions import IsAuthenticated


from . import serializers
from .models import User

from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rooms.models import Room
from rooms.serializers import RoomListSerializer

class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(user)
        
        return Response(serializer.data)
    
    def put(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(user, data=request.data,partial=True,)
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class Users(APIView):

    def post(self, request):
        password = request.data.get('password')
        if not password:
            raise ParseError
        
        serializer = serializers.PrivateUserSerializer(data = request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class PublicUser(APIView):
    
    def get(self,request, username):

        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            raise NotFound
        
        serializer = serializers.PublicUserSerializer(user)
        return Response(serializer.data)
    
class PublicUserReviews(APIView):
    def get(self, request, username):
        reviews = Review.objects.filter(user__username=username)
        serializer = ReviewSerializer(reviews, many=True,)
        return Response(serializer.data)

class PublicUserRooms(APIView):
    def get(self, request, username):
        rooms = Room.objects.filter(owner__username=username)
        serializer = RoomListSerializer(rooms, many=True,context={"request":request},)
        return Response(serializer.data)


    
class ChangePassword(APIView):

    permission_classes = [IsAuthenticated]
    
    def put(self,request):
        user = request.user
        old_pw = request.data.get('old_password')
        new_pw = request.data.get('new_password')
        if not old_pw or not new_pw:
            raise ParseError
        if user.check_password(old_pw):
            user.set_password(new_pw)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            raise ParseError

class LogIn(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            raise ParseError
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({"ok":'Welcome!'})
        else:
            return Response({"error":"wrong Password"},status=status.HTTP_400_BAD_REQUEST)
        
class LogOut(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        print("로그아웃 테스트 request ;",request)
        sleep(1)
        logout(request)
        return Response({"ok": "bye!"})

class JWTLogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            token = jwt.encode(
                {"pk": user.pk},
                settings.SECRET_KEY,
                algorithm="HS256",
            )
            return Response({"token": token})
        else:
            return Response({"error": "wrong password"})
class GithubLogin(APIView):
    def post(self, request):
        try:
            code = request.data.get('code')
            access_token = requests.post(f'https://github.com/login/oauth/access_token?code={code}&client_id=Ov23licVYLUaPAnys6tz&client_secret={settings.GH_SECRET}', headers={"Accept":"application/json"},).json().get("access_token")
            user_data = requests.get("https://api.github.com/user", headers={"Authorization":f"Bearer {access_token}", "Accept":"application/json",},).json()
            user_email = requests.get("https://api.github.com/user/emails", headers={"Authorization":f"Bearer {access_token}", "Accept":"application/json",},).json()
            try:
                user = User.objects.get(email = user_email[0]['email'])
                login(request,user)
                return Response(status=status.HTTP_200_OK)
            except User.DoesNotExist:
                user = User.objects.create(
                    username = user_data.get('login'),
                    email = user_email[0]['email'], 
                    name=user_data.get("name"),
                    avatar = user_data.get("avatar_url"),
                )
                user.set_unusable_password()
                user.save()
                login(request,user)
                return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
class KakaoLogin(APIView):
    def post(self, request):
        try:
            code = request.data.get("code")
            access_token = requests.post(
                "https://kauth.kakao.com/oauth/token",
                headers={ "Content-Type": "application/x-www-form-urlencoded", },
                data ={"grant_type":"authorization_code",
                    "client_id":"1af4b8b450dffcdd625ba1f8ca864120",
                    "redirect_uri":"http://127.0.0.1:3000/social/kakao",
                    "code":code},).json().get("access_token")
            user_data = requests.get(
                "https://kapi.kakao.com/v2/user/me",
                headers = {"Authorization":f"Bearer {access_token}",
                           "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"}).json()
            kakao_account = user_data.get("kakao_account")
            profile = kakao_account.get("profile")
            
            
            try:
                user = User.objects.get(email = kakao_account.get("email"))
                login(request,user)
                return Response(status=status.HTTP_200_OK)
            except User.DoesNotExist:
                user = User.objects.create(
                    username = profile.get("nickname"),
                    email = kakao_account.get("email"), 
                    name=profile.get("nickname"),
                    avatar = profile.get("profile_image_url"),
                )
                user.set_unusable_password()
                user.save()
                login(request,user)
                return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)