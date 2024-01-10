from django.db import transaction

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError,PermissionDenied
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Perk,Experience
from .serializers import PerkSerializer,ExperienceDetailSerialier,ExperienceListSerializer

from categories.models import Category

class Experiences(APIView):
    
    def get(self, request):
        
        permission_classes = [IsAuthenticatedOrReadOnly]

        all_experiences = Experience.objects.all()
        serializer = ExperienceListSerializer(all_experiences, many=True, context={"request":request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ExperienceDetailSerialier(data=request.data)
        if serializer.is_valid():
            category_pk = request.data.get('category')
            if not category_pk:
                raise ParseError("Category is required")
            try:
                category = Category.objects.get(pk=category_pk)
                if category.kind == Category.CategoryKindChoices.ROOMS:
                    raise ParseError("The category kind should be EXPERIENCES")
            except Category.DoesNotExist:
                raise ParseError("category not found.")
            
            # 트랜색션 시작
            try:
                with transaction.atomic():
                    experience=serializer.save(host=request.user,category=category,)
                    print('experience',experience)
                    perks = request.data.get("perks")
                    print('perks',perks)
                    print('perks?')
                    print('perk test',Perk.objects.get(pk=perks[0]))
                    print('perks?')
                    for perk_pk in perks:
                        print('perk !',perk)
                        perk = Perk.objects.get(pk=perk_pk)
                        print('add !')
                        experience.perks.add(perk)
                    print('end for')
                    serializer = ExperienceDetailSerialier(experience)
                    print('serializer',serializer)
                    return Response(serializer.data)
            except Exception:
                raise ParseError("Perks not found")
        else:
            return Response(serializer.errors)

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
