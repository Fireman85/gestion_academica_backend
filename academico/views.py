from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate
from .models import Programa
from .serializers import ProgramaSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets


class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer

# class ProgramaView(APIView):
#     def get(self, request, id=None):

#         programas_queryset = Programa.objects.all()
#         serializer = ProgramaSerializer(programas_queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # POST - Crear un nuevo programa
#     def post(self, request):
#         serializer = ProgramaSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # PUT - Modificar un nuevo programa
#     def put(self, request, id):
#         programa = get_object_or_404(Programa, id=id)
#         serializer = ProgramaSerializer(programa, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(
#             serializer.errors,
#             status=status.HTTP_404_NOT_FOUND
#         )

#     # DELETE - Borrar un nuevo programa
#     def delete(self, request, id):
#         programa = get_object_or_404(Programa, id=id)
#         programa.delete()
#         return Response({
#             "mensaje": "Programa eliminado correctamente"
#           },
#           status=status.HTTP_200_OK
#         )


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            return Response(
                {
                    "mensaje": "Autenticación satisfactoria"
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "error": "Error en la autenticación"
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
