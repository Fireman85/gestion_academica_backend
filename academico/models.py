from django.db import models


class Programa(models.Model):
    nombre_programa = models.CharField(max_length=120)
    nivel = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_programa


class Ficha(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    numero_ficha = models.CharField(max_length=20)
    jornada = models.CharField(max_length=30)
    programa = models.ForeignKey(Programa, on_delete=models.PROTECT)

    def __str__(self):
        return self.numero_ficha
