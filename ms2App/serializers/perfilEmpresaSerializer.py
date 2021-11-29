from ms2App.models.perfilEmpresa import PerfilEmpresa, Vacante
from rest_framework import serializers


class VacanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacante
        fields = '__all__'


class PerfilEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilEmpresa
        fields = ['vacantes',
                  'calificacion', 'añoCreacion', 'usuario']
