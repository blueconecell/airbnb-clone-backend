from django.db import transaction

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError,PermissionDenied
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Perk,Experience
from .serializers import PerkSerializer,ExperienceDetailSerialier,ExperienceListSerializer

from categories.models import Category

class Experiences(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
    
        all_experiences = Experience.objects.all()
        serializer = ExperienceListSerializer(all_experiences, many=True, context={"request":request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ExperienceDetailSerialier(data=request.data)
        if serializer.is_valid():
            category_pk = request.data.get('category')
            perk_pks = request.data.get('perks')
            if not category_pk:
                raise ParseError("Category is required")
            try:
                category = Category.objects.get(pk=category_pk)
                if category.kind != Category.CategoryKindChoices.EXPERIENCES:
                    raise ParseError("The category's kind should be EXPERIENCES")
            except Category.DoesNotExist:
                raise ParseError("category not found.")
            
            # 트랜색션 시작
            try:
                with transaction.atomic():
                    experience=serializer.save(host=request.user,category=category,)
                    print('experience',experience)
                    if perk_pks:
                        for perk_pk in perk_pks:
                            perk = Perk.objects.get(pk=perk_pk)
                            experience.perks.add(perk)
            except Perk.DoesNotExist:
                raise ParseError("Perks not found")
            except Exception as e:
                raise ParseError(e)
            serializer = ExperienceDetailSerialier(experience,context={'request':request},)
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST,)

class ExperienceDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self,pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):

        experience = self.get_object(pk)
        serializer = ExperienceDetailSerialier(experience, context={"request":request})
        return Response(serializer.data)

    def put(self, request, pk):
        experience = self.get_object(pk)
        if experience.host != request.user:
            raise PermissionDenied
        serializer = ExperienceDetailSerialier(experience, data=request.data, partial=True)
        if serializer.is_valid():
            category_pk = request.data.get('category')
            if category_pk:
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category.kind != Category.CategoryKindChoices.EXPERIENCES:
                        raise ParseError("The Category kind should be 'experience'")
                except Category.DoesNotExist:
                    raise ParseError("Category not found.")
            
            # 트랜섹션 시작!
            try:
                with transaction.atomic():
                    if category_pk:
                        updated_experience = serializer.save(category=category)
                    else:
                        updated_experience = serializer.save()
                    
                    perks = request.data.get('perks')
                    if perks:
                        updated_experience.perks.clear()

                        for perk_pk in perks:
                            perk = Perk.objects.get(pk=perk_pk)
                            updated_experience.perks.add(perk)
                    else:
                        updated_experience.perks.clear()
                    
            except Perk.DoesNotExist:
                raise ParseError("Perk not found.")
            except Exception as e:
                raise ParseError(e)
            serializer = ExperienceDetailSerialier(updated_experience,context={"request":request},)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



    
    def delete(self, request, pk):
        experience = self.get_object(pk)
        if experience.host != request.host:
            raise PermissionDenied
        experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Perks(APIView):


    def get(self, request):
        all_perks = Perk.objects.all()
        serialzer = PerkSerializer(all_perks,many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = PerkSerializer(data=request.data)
        if serializer.is_valid():
            perk = serializer.save()
            return Response(PerkSerializer(perk).data)
        else:
            return Response(serializer.errors)

class PerkDetial(APIView):

    def get_object(self, pk):
        try:
            return Perk.objects.get(pk=pk)
        except Perk.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(perk)
        return Response(serializer.data)

    def put(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(perk, data=request.data, partial=True)
        if serializer.is_valid():
            updated_perk = serializer.save()
            return Response(PerkSerializer(updated_perk).data)
        else:
            return Response(serializer.errors)
    def delete(self, request, pk):
        perk = self.get_object(pk)
        perk.delete()
        return Response(status=HTTP_204_NO_CONTENT)
