from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Formation
from .serializers import FormationSerializer


@api_view(['GET'])
def home(request: HttpRequest) -> HttpResponse:
    user = {
        "name": "Quentin",
        "age": 30
    }
    return JsonResponse(user)


@api_view(['GET', 'POST'])
def formations(request) -> HttpResponse:
    if request.method == "GET":
        formations = Formation.objects.all()
        serialized_formations = FormationSerializer(formations, many=True)
        return Response(serialized_formations.data)
    
    elif request.method == "POST":
        new_formation = FormationSerializer(data=request.data)
        if new_formation.is_valid():
            new_formation.save()
            return Response({ "message": "Formation créée !" })
        else:
            return Response({ "error": request.data })
        
    return Response()


@api_view(['GET', 'PUT', 'DELETE'])
def formation(request, pk: int) -> HttpResponse:
    if request.method == "GET":
        formation = Formation.objects.get(id=pk)
        serialized_formation = FormationSerializer(formation, many=False)
        return Response(serialized_formation.data)
    
    elif request.method == "PUT":
        formation = Formation.objects.get(id=pk)
        updated_formation = FormationSerializer(instance=formation, data=request.data)
        if updated_formation.is_valid():
            updated_formation.save()
            return Response({ "message": "Formation modifiée !" })
        else:
            return Response({ "error": "Mauvais body..." })
    
    elif request.method == "DELETE":
        formation = Formation.objects.get(id=pk)
        formation.delete()
        return Response({ "message": "Formation supprimée !" })

    return Response()

