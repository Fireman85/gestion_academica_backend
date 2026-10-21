from rest_framework import serializers
from .models import Programa, Ficha


class ProgramaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Programa
        fields = "__all__"

    def validate_nombre_programa(self, value):

        if len(value) < 5:
            raise serializers.ValidationError("El nombre del programa debe tener mínimo 5 caracteres")

        return value

    def validate_nivel(self, value):
        niveles_permitidos = [
            "Técnico",
            "Tecnólogo",
            "Especialización",
        ]

        if value not in niveles_permitidos:
            raise serializers.ValidationError(
                "El nivel debe ser: Técnico, Tecnólogo o  Especialización"
            )
        return value


class FichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha
        fields = "__all__"
