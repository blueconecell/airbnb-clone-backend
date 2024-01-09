from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from .models import Perk,Experience
from .serializers import PerkSerializer,ExperienceDetailSerialier,ExperienceListSerializer

class Experiences(APIView):
    
    def get(self, request):
        
        permission_classes = [IsAuthenticatedOrReadOnly]

        all_experiences = Experience.objects.all()
        serializer = ExperienceListSerializer(all_experiences, many=True, context={"request":request})
        return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = ExperienceDetailSerialier(data=request.data)
    #     if serializer.is_valid():
    #         category_pk = request.data.get('category')


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
