from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from ms2App.models.proyecto import Proyectos
from ms2App.serializers.proyectoSerializer import ProyectoSerializer
from bson import ObjectId


@api_view(['GET', 'POST'])
def proyecto_view(request):

    if request.method == 'GET':
        proyectos = Proyectos.objects.all()
        proyecto_serializer = ProyectoSerializer(proyectos, many=True)
        return Response(proyecto_serializer.data)

    elif request.method == 'POST':
        proyecto_serializer = ProyectoSerializer(data=request.data)
        if proyecto_serializer.is_valid():
            proyecto_serializer.save()
            return Response(proyecto_serializer.data)
        return Response(proyecto_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def proyecto_detail_view(request, pk=None):
    id = ObjectId(pk)
    # preguntar si al no haber propiamente una pk, llegarian todos los de todos los usuarios
    proyecto = Proyectos.objects.filter(pk=id).first()

    if proyecto:

        if request.method == 'GET':
            proyecto_serializer = ProyectoSerializer(proyecto)
            return Response(proyecto_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            proyecto_serializer = ProyectoSerializer(
                proyecto, data=request.data)
            if proyecto_serializer.is_valid():
                proyecto_serializer.save()
                return Response(proyecto_serializer.data, status=status.HTTP_200_OK)
            return Response(proyecto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            proyecto.delete()
            return Response({'message': 'proyecto eliminado'}, status.HTTP_200_OK)

    return Response({'message': 'proyecto no encontrado'}, status=status.HTTP_400_BAD_REQUEST)
