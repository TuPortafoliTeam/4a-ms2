from rest_framework import serializers
from ms2App.models import Perfil, Formacion, Trabajo


class TrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajo
        fields = '__all__'


class FormacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formacion
        fields = '__all__'


class PerfilSerializer(serializers.ModelSerializer):
    formacion = [FormacionSerializer()]
    trabajo = [TrabajoSerializer()]

    class Meta:
        model = Perfil
        fields = '__all__'
