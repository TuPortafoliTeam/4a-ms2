from ms2App.models.proyecto import Proyectos, Tecnologia, Duracion, Enlaces
from rest_framework import serializers


class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = '__all__'


class DuracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duracion
        fields = '__all__'


class EnlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enlaces
        fields = '__all__'


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyectos
        fields = '__all__'
