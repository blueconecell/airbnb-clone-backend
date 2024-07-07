from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.shortcuts import get_object_or_404

from medias.serializers import PhotoSerializer
from rooms.models import Room
from .models import Photo

class PhotoDetail(APIView):

    permission_classes = [IsAuthenticated]
    def get_object(self,pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise NotFound

    def delete(self, request, pk):
        photo = self.get_object(pk)
        if (photo.room and photo.room.owner != request.user) or (
            photo.experience and photo.experience.host != request.user):
            raise PermissionDenied
        photo.delete()
        return Response(status=HTTP_200_OK)

class UploadImg(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,pk):
        print("request",request)
        print("request.data",request.data)
        room = get_object_or_404(Room, pk=pk)
        data = request.data.copy()
        data['room'] = room.pk
        serializer = PhotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

