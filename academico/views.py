from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate
from .models import Programa
from .serializers import ProgramaSerializer


class ProgramaView(APIView):
    def get(self, request, id=None):

        programas_queryset = Programa.objects.all()
        serializer = ProgramaSerializer(programas_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
